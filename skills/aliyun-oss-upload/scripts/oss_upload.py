#!/usr/bin/env python3
"""Upload a file to Aliyun OSS without storing credentials in Git.

Configuration priority:
1. Environment variables documented in the repository README.
2. An ignored sibling ``config.json`` created from ``config.example.json``.
"""

import json
import os
import sys
import hashlib
from datetime import datetime

def load_config():
    """Load environment configuration first, then the ignored local config."""
    env_config = {
        'region': os.environ.get('ALIYUN_OSS_REGION', '').strip(),
        'bucket': os.environ.get('ALIYUN_OSS_BUCKET', '').strip(),
        'accessKeyId': os.environ.get('ALIYUN_ACCESS_KEY_ID', '').strip(),
        'accessKeySecret': os.environ.get('ALIYUN_ACCESS_KEY_SECRET', '').strip(),
    }
    if all(env_config.values()):
        return env_config

    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.json'))
    try:
        with open(config_path, encoding='utf-8') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {}

    merged = {key: env_config[key] or str(config.get(key, '')).strip() for key in env_config}
    missing = [key for key, value in merged.items() if not value]
    if missing:
        message = (
            f"ERROR: missing OSS configuration: {', '.join(missing)}\n"
            "Set ALIYUN_OSS_REGION, ALIYUN_OSS_BUCKET, ALIYUN_ACCESS_KEY_ID, and\n"
            "ALIYUN_ACCESS_KEY_SECRET, or create an ignored config.json from config.example.json."
        )
        print(message, file=sys.stderr)
        sys.exit(2)
    return merged

# 所有文件统一上传到 img/ 目录下
OSS_PREFIX = 'img'

def get_content_type(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    types = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.webp': 'image/webp',
        '.svg': 'image/svg+xml',
        '.pdf': 'application/pdf',
        '.mp4': 'video/mp4',
        '.mp3': 'audio/mpeg',
        '.txt': 'text/plain',
    }
    return types.get(ext, 'application/octet-stream')

def get_oss_url(bucket, region, object_name):
    # 标准公开访问 URL
    return f"https://{bucket}.{region}.aliyuncs.com/{object_name}"

def upload_file(file_path, object_name=None):
    config = load_config()
    try:
        import oss2
    except ImportError:
        print("ERROR: oss2 package not installed. Run: pip install oss2")
        sys.exit(1)

    auth = oss2.Auth(config['accessKeyId'], config['accessKeySecret'])
    # endpoint 只需要区域部分，oss2 会自动拼接 bucket.region.aliyuncs.com
    endpoint = f"{config['region']}.aliyuncs.com"
    bucket = oss2.Bucket(auth, endpoint, config['bucket'])

    file_path = os.path.abspath(file_path)

    if not os.path.exists(file_path):
        print(f"ERROR: File not found: {file_path}")
        sys.exit(1)

    if object_name is None:
        # 自动生成文件名：前缀/时间戳_原文件名
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        original_name = os.path.basename(file_path)
        ext = os.path.splitext(original_name)[1]
        object_name = f"{OSS_PREFIX}/{timestamp}_{hashlib.md5(original_name.encode()).hexdigest()[:8]}{ext}"

    content_type = get_content_type(file_path)

    with open(file_path, 'rb') as f:
        result = bucket.put_object(object_name, f, headers={'Content-Type': content_type})

    if result.status == 200:
        oss_url = get_oss_url(config['bucket'], config['region'], object_name)
        print(oss_url)
    else:
        print(f"ERROR: Upload failed with status {result.status}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] in {'-h', '--help'}:
        print('Usage: oss_upload.py <file_path> [oss_object_name]')
        print('Configuration: environment variables or ignored ../config.json')
        sys.exit(0)

    if len(sys.argv) < 2:
        print("Usage: oss_upload.py <file_path> [oss_object_name]")
        sys.exit(1)

    file_path = sys.argv[1]
    object_name = sys.argv[2] if len(sys.argv) > 2 else None
    upload_file(file_path, object_name)
