---
name: yoyo-gzh
description: Analyze a Chinese article topic and produce a publishable WeChat package with a question-led WeChat draft, detailed blog draft, article-specific YOYO cover, YOYO v2 body illustrations with optional numbered hand-drawn styles, OSS image URLs, and copy-ready WeChat HTML. Use when the user asks to turn a topic, idea, headline, trend, question, or rough notes into a complete WeChat and blog publication package.
---

# YOYO GZH

## Overview

Turn one article topic into a two-channel publication package:

- a WeChat Markdown draft around 1500 Chinese characters
- a WeChat HTML layout generated with `gzh-design`
- a more detailed blog Markdown draft
- an article-specific WeChat cover with the title and YOYO IP in a clear left-right composition
- YOYO v2 article illustrations, optionally fused with a `001`–`279` numbered hand-drawn style, uploaded to Aliyun OSS
- final Markdown files with OSS image URLs already embedded

Use this skill as an orchestration workflow. It relies on companion skills for writing voice, illustration generation, image hosting, and WeChat visual layout.

## Companion Skills

Load and follow these skills during execution:

- `human-writing` for final article voice, factual-material checks, revision, and self-check.
- `imagegen` for the YOYO cover. Use the canonical YOYO reference assets from `yoyo-illustrations` and the built-in image generation mode unless the user explicitly chooses another supported path.
- `yoyo-illustrations` v2 as the sole planner and generator for 16:9 body illustrations. It owns built-in `imagegen`, YOYO identity references, optional numbered hand-drawn style resolution, blend strength, dual-reference isolation, and image QA.
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
- requested body-illustration style (`native-yoyo` or hand-drawn style `001`–`279`) and blend strength (`safe`, `balanced`, or `full`), if any

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

### 5. Polish With Human-Writing

Apply `human-writing` after the core argument and its supporting material are already formed. Preserve the user's intended stance and facts. For non-fiction, do not invent personal experiences, scenes, quotations, or data to make the draft feel more vivid.

Emphasize:

- a concrete speaker who knows what they know and acknowledges what remains uncertain
- direct judgment supported by specific, verifiable material
- natural Chinese rhythm, varied paragraph length, and forward movement between sections
- honest treatment of uncertainty, tradeoffs, and the limits of the evidence

Read the task-relevant `human-writing` references before drafting and `references/revision.md` after the first draft. Respect its hard language constraints in the final WeChat and blog drafts, unless the user's publication format requires otherwise.

### 6. Fill the Cover Brief and Generate the YOYO Cover

Generate one cover for a complete publication package unless the user declines a cover or explicitly requests another cover workflow.

Read [`references/yoyo-cover.md`](references/yoyo-cover.md) after the final article title and core thesis are stable. Infer and save the cover brief, then generate the cover with `imagegen` using the canonical YOYO reference assets from `yoyo-illustrations`.

Required cover composition:

- keep the final article title visible on the cover; preserve its exact wording unless the user explicitly approves different cover text
- use a left-right layout, with title text on the left and YOYO on the right by default
- keep the title and YOYO in separate safe areas so neither overlaps, covers, or crowds the other
- size YOYO's visible figure to about 25%-30% of the canvas width
- make YOYO perform one article-specific action or interact with one article-specific object that expresses the core tension, consequence, or promise
- make the cover interesting enough to invite a click through a clear visual question, contrast, or unresolved moment, without misleading clickbait

Do not fall back to the former minimalist big-tech cover system, abstract logo-like anchors, generic technology gradients, or an unrelated mascot pose.

Save the local cover as:

```text
assets/<slug>-cover.png
```

Save the filled brief as:

```text
outputs/<slug>-cover-brief.md
```

Upload the final cover with `aliyun-oss-upload` and record the public URL in the cover brief. If upload fails, keep the local PNG, report the failure, and do not claim that the cover is publication-ready.

### 7. Plan and Generate Body Illustrations With YOYO v2

Use `yoyo-illustrations` v2 on the final article content, not on an early outline. It is the sole owner of body-illustration prompting and generation: do not assemble a parallel YOYO prompt in this Skill, do not call `imagegen` directly for body images, and do not invoke `handdraw-style-prompter` separately.

Create one unified shot list selected by cognitive value: core thesis, key contrast, mechanism or loop, turning point, and risk or tradeoff. Use 2–4 of the strongest images in the WeChat version; the blog may reuse those and add images up to its 3–6 target. Do not generate duplicate images merely because both drafts use them.

Pass illustration preferences to YOYO v2 unchanged:

- no style specified: use `native-yoyo`
- numbered style specified: pass the normalized `001`–`279` number
- numbered style without blend strength: use YOYO v2's default `balanced`
- explicit `safe`, `balanced`, or `full`: preserve it
- layout ID such as `SC-008` specified: resolve it as a layout reference, not as a `001`–`279` illustration-style number. Pass its composition guidance to YOYO v2 while preserving YOYO identity and any separate style preference. If the user requests no image text, omit the layout's text slot.

YOYO v2 must use built-in `imagegen`, choose the canonical character reference, add a numbered style reference only when its resolver requires one, and complete its identity/content/style QA before an image is accepted.

Generate separate 16:9 PNG files under:

```text
assets/<slug>-illustrations/
```

Use ordered filenames such as:

```text
01-core-question.png
02-hidden-mechanism.png
```

Do not create decorative filler images. Each image must explain one idea and place YOYO in the core action. Record the accepted rendering mode, style number and name, blend strength, and whether a numbered style reference image was used; these details belong in the final execution report, not in the article captions.

### 8. Upload Images and Embed URLs

Use `aliyun-oss-upload` for every final image. Capture the returned public URL.

Replace local image paths in both Markdown drafts with the OSS URLs:

```markdown
![简短中文图注](https://...)
```

If upload fails, leave local image paths in the drafts, report the failure, and do not pretend the files are publication-ready.

For YOYO body illustrations, retain concise Markdown alt text for accessibility, but render no visible image title or caption beneath the image in the WeChat HTML. An illustration's alt text is not a request for a visible caption.

### 9. Select GZH Theme

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

### 10. Generate WeChat HTML With GZH Design

After the final WeChat Markdown has OSS image URLs embedded, use `gzh-design` to produce a copy-ready WeChat HTML preview with the selected theme.

Follow `gzh-design` requirements:

- read its `references/theme-index.md`
- read the selected theme component file
- read `references/common-components.md`
- generate the clean HTML fragment and preview wrapper
- run `scripts/validate_gzh_html.py` until ERROR is 0
- fix half-width punctuation warnings where they affect article text

The WeChat Markdown remains one of the final deliverables. The HTML/preview files are additional publishing assets for pasting into the WeChat editor.

### 11. Save Deliverables

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
- the filled cover brief and local cover PNG exist unless the user declined the cover
- the cover uses the requested ratio and contains the exact final article title with no unapproved extra text
- the title and YOYO use a clean left-right layout with no overlap; YOYO's visible figure occupies about 25%-30% of the canvas width
- YOYO matches the canonical IP and performs an article-specific action that creates a clear, truthful reason to click
- the cover is uploaded to OSS when upload credentials are available
- the WeChat version is close to 1500 Chinese characters
- the blog version is more detailed than the WeChat version
- both titles are question-style or clearly question-led
- each opening answers the question directly
- social, humanities, economy, and technology lenses all appear in the analysis
- generated images are embedded with OSS URLs when upload succeeded
- every accepted body image passed YOYO v2 identity/content QA and, when applicable, numbered-style QA
- the final report identifies `native-yoyo` or the numbered style, blend strength, and whether a numbered style reference image was used
- `gzh-design` theme was selected by user request or the default mapping above
- WeChat HTML validation passed with 0 ERROR when HTML generation succeeded
- unresolved missing credentials, failed uploads, failed image generation, or failed HTML layout generation are reported plainly
