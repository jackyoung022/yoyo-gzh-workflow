---
name: aliyun-oss-upload
description: Upload local files to Aliyun OSS and return a public URL. Credentials are always loaded from environment variables or an ignored local configuration file.
---

# Aliyun OSS Upload

Use this companion skill only after illustration files have passed QA.

## Safe configuration

Preferred method: set these environment variables in the shell that runs the upload:

```bash
export ALIYUN_OSS_REGION="oss-cn-hangzhou"
export ALIYUN_OSS_BUCKET="your-public-bucket"
export ALIYUN_ACCESS_KEY_ID="your-access-key-id"
export ALIYUN_ACCESS_KEY_SECRET="your-access-key-secret"
```

Alternatively, copy `config.example.json` to `config.json` in this directory and replace its placeholders. `config.json` is ignored by Git and must never be committed.

Create a least-privilege RAM user or STS credential with write access only to the target OSS prefix. The target bucket must allow the resulting objects to be publicly readable if public image URLs are required.

## Usage

```bash
python3 -m pip install -r requirements.txt
python3 skills/aliyun-oss-upload/scripts/oss_upload.py assets/example.png articles/example/01-core-question.png
```

The command prints only the public URL on success. Use the URL in both Markdown drafts:

```markdown
![简短图注](https://your-public-bucket.oss-cn-hangzhou.aliyuncs.com/articles/example/01-core-question.png)
```

If an upload fails, keep the local path in the draft and report that the package is not publication-ready.
