#!/usr/bin/env python3
"""Fail when likely credentials are found in tracked project files.

This is a lightweight local guard, not a replacement for provider-side secret
scanning or immediate credential rotation after an exposure.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_NAMES = {".git", "__pycache__", ".DS_Store"}
EXCLUDED_PATHS = {
    ROOT / ".env.example",
    ROOT / "skills" / "aliyun-oss-upload" / "config.example.json",
}
PATTERNS = {
    "Aliyun AccessKey ID": re.compile(r"\bLTAI[A-Za-z0-9]{12,}\b"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Google API key": re.compile(r"\bAIza[\w-]{20,}\b"),
    "GitHub personal token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
}


def is_text(path: Path) -> bool:
    try:
        sample = path.read_bytes()[:4096]
    except OSError:
        return False
    return b"\0" not in sample


def main() -> int:
    findings: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in EXCLUDED_NAMES for part in path.parts):
            continue
        if path in EXCLUDED_PATHS or not is_text(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{path.relative_to(ROOT)}:{line}: possible {label}")

    if findings:
        print("Secret scan failed:", file=sys.stderr)
        print("\n".join(findings), file=sys.stderr)
        return 1
    print("Secret scan passed: no likely committed credentials found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
