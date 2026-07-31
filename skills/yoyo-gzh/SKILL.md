---
name: yoyo-gzh
description: Analyze a user-provided Chinese article topic, research it when needed, develop a cross-disciplinary angle, and produce a publishable WeChat official account package plus a detailed blog Markdown draft. Use when the user asks to turn a topic, idea, headline, trend, question, or rough notes into a question-led article package with social, humanities, economic, and technology analysis, Khazix-style polishing, YOYO-style illustrations, Aliyun OSS image URLs, gzh-design WeChat HTML layout, and final WeChat/blog Markdown files.
---

# YOYO GZH

## Overview

Turn one article topic into a two-channel publication package:

- a WeChat Markdown draft around 1500 Chinese characters
- a WeChat HTML layout generated with `gzh-design`
- a more detailed blog Markdown draft
- YOYO-style article illustrations uploaded to Aliyun OSS
- final Markdown files with OSS image URLs already embedded

Use this skill as an orchestration workflow. It relies on companion skills for writing voice, illustration generation, image hosting, and WeChat visual layout.

## Companion Skills

Load and follow these skills during execution:

- `khazix-writer` for final article voice, rhythm, hooks, and self-check.
- `yoyo-illustrations` for planning and generating 16:9 Chinese article illustrations.
- `aliyun-oss-upload` for uploading each generated image and obtaining public URLs.
- `gzh-design` for turning the final WeChat Markdown into copy-ready WeChat HTML.

If a companion skill cannot be loaded or its required credentials are missing, continue with the parts that can be completed and clearly report the blocked step.

## Workflow

### 1. Clarify the Topic

Extract or infer:

- core topic
- target reader
- publication context
- likely controversy or tension
- preferred point of view if the user supplied one
- requested `gzh-design` theme, if any

Ask only when a missing detail would materially change the article. Otherwise make a reasonable assumption and state it briefly.

Create a short slug in lowercase letters, digits, and hyphens for filenames and image folders.

### 2. Research and Cross-Disciplinary Analysis

Use web research when the topic depends on current facts, market conditions, new products, policy, public figures, recent cultural events, or any unstable information. Prefer primary or high-quality sources.

Analyze the topic from at least four lenses:

- society: institutions, groups, incentives, norms, public mood
- humanities: history, philosophy, psychology, narrative, values
- economy: business model, costs, markets, labor, distribution of gains and losses
- technology: enabling technologies, constraints, adoption curve, technical risk

Keep source URLs and concrete facts available for the drafts. Do not overload the WeChat version with citations; include enough links or a short source note in the blog version when useful.

### 3. Build the Question-Led Angle

Generate several question-style title candidates. Choose one that is specific, debatable, and answerable.

The opening must answer the title question directly before expanding the analysis. Use this pattern:

1. first paragraph gives the direct answer
2. next paragraph names the hidden tension
3. body then拆解 the issue layer by layer

Avoid titles that are only rhetorical, vague, or clickbait without a real answer.

### 4. Draft Two Versions

Write the WeChat version first:

- target length around 1500 Chinese characters, acceptable range 1200-1800
- strong opening hook
- compact structure, fewer citations, more narrative momentum
- 2-4 body illustrations
- suitable for public-account reading on mobile

Then write the blog version:

- more detailed than the WeChat version, normally 2500-5000 Chinese characters unless the user asks otherwise
- keep the same core thesis but add context, evidence, tradeoffs, and counterarguments
- 3-6 body illustrations when the length supports them
- include source links or a short references section when factual claims rely on external research

### 5. Polish With Khazix Style

Apply `khazix-writer` after the core argument is already formed. Preserve the user's intended stance and facts.

Emphasize:

- "有见识的普通人在认真聊一件打动他的事"
- direct judgment before abstract explanation
- lively human rhythm, short paragraphs, and hooks between sections
- honesty about uncertainty and tradeoffs

Respect Khazix language constraints unless the user's publication format requires otherwise.

### 6. Plan and Generate Illustrations

Use `yoyo-illustrations` on the final article content, not on an early outline.

Select image points by cognitive value:

- core thesis
- key contrast
- mechanism or loop
- turning point
- risk or tradeoff

Generate separate 16:9 PNG files under:

```text
assets/<slug>-illustrations/
```

Use ordered filenames such as:

```text
01-core-question.png
02-hidden-mechanism.png
```

Do not create decorative filler images. Each image must explain one idea and place YOYO in the core action.

### 7. Upload Images and Embed URLs

Use `aliyun-oss-upload` for every final image. Capture the returned public URL.

Replace local image paths in both Markdown drafts with the OSS URLs:

```markdown
![简短中文图注](https://...)
```

If upload fails, leave local image paths in the drafts, report the failure, and do not pretend the files are publication-ready.

### 8. Select GZH Theme

Use the user's requested `gzh-design` theme when explicitly specified.

If the user does not specify a theme, choose by topic:

| Theme | Best for |
| --- | --- |
| 摸鱼绿 | 教程、测评、清单、工具盘点，卡片丰富、信息密度高 |
| 红白色系 | 深度分析、观点、力量感话题，经典编辑风 |
| 石墨极简风 | 设计、科技评论、专业观点、高端品牌 |
| 留白禅意风 | 禅意、极简生活、深度随笔，呼吸感最强 |
| 摸鱼票据风 | 工具对比、创意评测，票据视觉隐喻 |
| 橄榄手记 | 内刊手记、深度评测、案例复盘，编辑部内刊质感 |

Default decisions:

- Use `红白色系` for broad deep analysis, social issues, and strong opinion pieces.
- Use `石墨极简风` for AI, technology commentary, design, and professional viewpoints.
- Use `摸鱼绿` when the draft is primarily practical, list-like, or tool-oriented.
- If two themes both fit, choose the one that matches the article's emotional temperature and report the choice briefly.

### 9. Generate WeChat HTML With GZH Design

After the final WeChat Markdown has OSS image URLs embedded, use `gzh-design` to produce a copy-ready WeChat HTML preview with the selected theme.

Follow `gzh-design` requirements:

- read its `references/theme-index.md`
- read the selected theme component file
- read `references/common-components.md`
- generate the clean HTML fragment and preview wrapper
- run `scripts/validate_gzh_html.py` until ERROR is 0
- fix half-width punctuation warnings where they affect article text

The WeChat Markdown remains one of the final deliverables. The HTML/preview files are additional publishing assets for pasting into the WeChat editor.

### 10. Save Deliverables

Read `references/output-contract.md` before saving final files.

Save the final Markdown files as:

```text
outputs/<slug>-wechat.md
outputs/<slug>-blog.md
```

Save `gzh-design` HTML assets according to its own filename conventions, normally beside the generated article files or in the current workspace.

If the current workspace has a different established output directory, use that directory and report the exact paths.

## Quality Gate

Before final response, verify:

- both Markdown files exist
- the WeChat version is close to 1500 Chinese characters
- the blog version is more detailed than the WeChat version
- both titles are question-style or clearly question-led
- each opening answers the question directly
- social, humanities, economy, and technology lenses all appear in the analysis
- generated images are embedded with OSS URLs when upload succeeded
- `gzh-design` theme was selected by user request or the default mapping above
- WeChat HTML validation passed with 0 ERROR when HTML generation succeeded
- unresolved missing credentials, failed uploads, failed image generation, or failed HTML layout generation are reported plainly
