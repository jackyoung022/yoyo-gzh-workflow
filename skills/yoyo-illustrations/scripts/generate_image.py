#!/usr/bin/env python3
"""
YOYO Illustrations - Nano Banana Pro Image Generation Script

Calls Google's Nano Banana Pro API (Generative Language API) to generate
16:9 flat vector illustrations for Chinese articles.

Usage:
    python3 generate_image.py --prompt "your prompt" --output "path/to/output.png"

API Key (one of these must be set):
    1. Environment variable: GOOGLE_API_KEY
    2. Key file: ~/.config/yoyo-illustrations/api_key

Optional:
    --model MODEL_NAME    Override model (default: gemini-3-pro-image)
    --aspect-ratio RATIO  Aspect ratio (default: 16:9)
    --image-size SIZE     Image size: 1K/2K/4K (default: 2K)
    --base-url URL        Override API base URL (for proxies)
    --reference PATH      Reference image for character consistency
                          (default: assets/yoyo-ip-front.png in skill dir)
    --no-reference        Disable reference image upload
"""

import argparse
import base64
import json
import os
import sys
from pathlib import Path

try:
    import urllib.request
    import urllib.error
except ImportError:
    print("Error: urllib is required (Python 3 standard library)", file=sys.stderr)
    sys.exit(1)

DEFAULT_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"
DEFAULT_MODEL = "gemini-3-pro-image"
DEFAULT_ASPECT_RATIO = "16:9"
DEFAULT_IMAGE_SIZE = "2K"
KEY_FILE = Path.home() / ".config" / "yoyo-illustrations" / "api_key"
PROXY_FILE = Path.home() / ".config" / "yoyo-illustrations" / "proxy"
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_REFERENCE = SCRIPT_DIR.parent / "assets" / "yoyo-ip-front.png"


def get_api_key():
    """Resolve API key from env var or key file."""
    key = os.environ.get("GOOGLE_API_KEY", "").strip()
    if key:
        return key

    if KEY_FILE.exists():
        key = KEY_FILE.read_text().strip()
        if key:
            return key

    return None


def get_proxy(proxy_arg=None):
    """Resolve proxy from CLI arg, env vars, or proxy file."""
    if proxy_arg:
        return proxy_arg

    for var in ("HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy", "ALL_PROXY", "all_proxy"):
        val = os.environ.get(var, "").strip()
        if val:
            return val

    if PROXY_FILE.exists():
        val = PROXY_FILE.read_text().strip()
        if val:
            return val

    return None


def generate_image(prompt, output_path, model=None, aspect_ratio=None,
                   image_size=None, base_url=None, mime_type="image/jpeg",
                   proxy=None, reference=None):
    """Call Nano Banana Pro API and save generated image."""

    api_key = get_api_key()
    if not api_key:
        print("Error: API key not found.", file=sys.stderr)
        print("", file=sys.stderr)
        print("Set it via one of:", file=sys.stderr)
        print(f"  1. export GOOGLE_API_KEY='your-key-here'", file=sys.stderr)
        print(f"  2. Save key to: {KEY_FILE}", file=sys.stderr)
        sys.exit(1)

    proxy = proxy or get_proxy()

    model = model or DEFAULT_MODEL
    aspect_ratio = aspect_ratio or DEFAULT_ASPECT_RATIO
    image_size = image_size or DEFAULT_IMAGE_SIZE
    base_url = base_url or DEFAULT_BASE_URL

    # Resolve reference image
    ref_path = None
    if reference is None:
        # Default: use the canonical YOYO front turnaround asset if it exists
        if DEFAULT_REFERENCE.exists():
            ref_path = DEFAULT_REFERENCE
    elif reference:
        ref_path = Path(reference)
        if not ref_path.exists():
            print(f"Warning: reference image not found: {ref_path}", file=sys.stderr)
            ref_path = None

    url = f"{base_url}/interactions"

    # Build input array with optional reference image
    input_items = []
    if ref_path:
        ref_bytes = ref_path.read_bytes()
        ref_b64 = base64.b64encode(ref_bytes).decode("utf-8")
        ref_mime = "image/png" if ref_path.suffix.lower() == ".png" else "image/jpeg"
        input_items.append({
            "type": "image",
            "mime_type": ref_mime,
            "data": ref_b64
        })
        print(f"Using reference: {ref_path.name} ({len(ref_bytes) / 1024:.0f} KB)")

    input_items.append({"type": "text", "text": prompt})

    payload = {
        "model": model,
        "input": input_items,
        "response_format": {
            "type": "image",
            "mime_type": mime_type,
            "aspect_ratio": aspect_ratio,
            "image_size": image_size
        }
    }

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    # Build opener with proxy if configured
    if proxy:
        proxy_handler = urllib.request.ProxyHandler({
            "http": proxy,
            "https": proxy
        })
        opener = urllib.request.build_opener(proxy_handler)
    else:
        opener = urllib.request.build_opener()

    try:
        with opener.open(req, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        print(f"API Error {e.code}: {e.reason}", file=sys.stderr)
        try:
            err = json.loads(error_body)
            msg = err.get("error", {}).get("message", error_body)
            print(f"Details: {msg}", file=sys.stderr)
        except json.JSONDecodeError:
            print(f"Details: {error_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}", file=sys.stderr)
        sys.exit(1)

    # Extract image data from response
    image_data = None

    # Path 1: convenience property
    output_image = result.get("output_image")
    if output_image and output_image.get("data"):
        image_data = output_image["data"]

    # Path 2: interactions API format — steps[].content[].data
    if not image_data:
        for step in result.get("steps", []):
            items = step.get("content") or step.get("parts") or []
            for item in items:
                if item.get("type") == "image" and item.get("data"):
                    image_data = item["data"]
                    break
            if image_data:
                break

    # Path 3: candidates (standard Gemini format fallback)
    if not image_data:
        for candidate in result.get("candidates", []):
            for part in candidate.get("content", {}).get("parts", []):
                inline = part.get("inline_data") or part.get("inlineData")
                if inline and inline.get("data"):
                    image_data = inline["data"]
                    break
            if image_data:
                break

    if not image_data:
        # Check for safety rejection
        for candidate in result.get("candidates", []):
            reason = candidate.get("finishReason", "")
            if reason in ("PROHIBITED_CONTENT", "SAFETY", "BLOCKED"):
                print(f"Generation blocked by safety filter: {reason}", file=sys.stderr)
                sys.exit(2)
        print("Error: No image data in response.", file=sys.stderr)
        print(f"Response keys: {list(result.keys())}", file=sys.stderr)
        sys.exit(1)

    # Save image
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    image_bytes = base64.b64decode(image_data)
    output.write_bytes(image_bytes)
    print(f"Saved: {output} ({len(image_bytes) / 1024:.0f} KB)")


def main():
    parser = argparse.ArgumentParser(
        description="Generate YOYO-style illustrations via Nano Banana Pro API"
    )
    parser.add_argument("--prompt", required=True, help="Image generation prompt")
    parser.add_argument("--output", required=True, help="Output file path (.png)")
    parser.add_argument("--model", default=None,
                        help=f"Model name (default: {DEFAULT_MODEL})")
    parser.add_argument("--aspect-ratio", default=None,
                        help=f"Aspect ratio (default: {DEFAULT_ASPECT_RATIO})")
    parser.add_argument("--image-size", default=None,
                        help=f"Image size: 1K/2K/4K (default: {DEFAULT_IMAGE_SIZE})")
    parser.add_argument("--base-url", default=None,
                        help=f"API base URL (default: {DEFAULT_BASE_URL})")
    parser.add_argument("--mime-type", default="image/jpeg",
                        help="Output MIME type (default: image/jpeg)")
    parser.add_argument("--proxy", default=None,
                        help="HTTP/SOCKS proxy URL (e.g. http://127.0.0.1:7890). "
                             "Also reads HTTPS_PROXY env var or "
                             "~/.config/yoyo-illustrations/proxy")
    parser.add_argument("--reference", default=None, nargs="?",
                        help="Path to reference image for character consistency. "
                             "Default: assets/yoyo-ip-front.png in skill dir")
    parser.add_argument("--no-reference", action="store_true",
                        help="Disable reference image upload")

    args = parser.parse_args()

    # Handle reference: --no-reference passes empty string to disable,
    # None means use default, explicit path overrides
    ref = args.reference
    if args.no_reference:
        ref = ""

    generate_image(
        prompt=args.prompt,
        output_path=args.output,
        model=args.model,
        aspect_ratio=args.aspect_ratio,
        image_size=args.image_size,
        base_url=args.base_url,
        mime_type=args.mime_type,
        proxy=args.proxy,
        reference=ref
    )


if __name__ == "__main__":
    main()
