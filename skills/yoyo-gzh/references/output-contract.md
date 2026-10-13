# Output Contract

Use this contract when saving final article drafts.

## Files

Create two required article Markdown files:

- `<slug>-wechat.md`
- `<slug>-blog.md`

Use the active workspace's `outputs/` directory when available.

When the cover workflow runs, also create:

- `outputs/<slug>-cover-brief.md`
- `assets/<slug>-cover.png` or a versioned sibling when needed

Upload the accepted cover to OSS and record its URL in the cover brief. The cover is a publishing asset and is not embedded as the first body image unless the user requests that layout.

Also create WeChat layout assets with `gzh-design` after the WeChat Markdown is finalized:

- a clean HTML fragment for fallback copying
- a preview HTML page with the copy button

These HTML files are publishing aids, not replacements for the required Markdown files.

## WeChat Markdown

Recommended structure:

```markdown
# <question-style title>

<opening paragraph that directly answers the title question>

![图注](https://oss-url)

## <short section heading>

...
```

Keep headings short. Avoid footnote-heavy formatting. Use images sparingly and place them after the paragraph they clarify.

After image URLs are embedded, pass this Markdown into `gzh-design` with the selected theme. If the user did not specify a theme, choose from the default mapping in `SKILL.md`.

## Blog Markdown

Recommended structure:

```markdown
# <question-style title>

<opening paragraph that directly answers the title question>

## <context or thesis section>

...

## 参考资料

- [source title](https://...)
```

Include a `参考资料` section when web research materially shaped the article.

## Image Rules

Generate body images only through `yoyo-illustrations` v2. `yoyo-gzh` chooses insertion points and article roles, then delegates prompt construction, built-in `imagegen`, YOYO character references, optional numbered-style references, blend strength, and QA to YOYO v2. Do not call `handdraw-style-prompter` or `imagegen` separately for body images.

Use OSS URLs in final Markdown when upload succeeded. Use local paths only when upload failed or the user explicitly asks for local-only drafts.

Use concise alt text that describes the idea, not the visual style. In WeChat HTML, YOYO body illustrations have no visible title or caption; the Markdown alt text remains an accessibility description only.

## Cover Rules

Follow `references/yoyo-cover.md`. The default cover brief uses a 5:2 ratio, the exact final article title, and a left-right composition with title text on the left and YOYO on the right. Keep separate safe areas so the title never overlaps the character. YOYO's visible figure should occupy about 25%-30% of the canvas width.

Tie YOYO's action and the accompanying article-specific object to the article's core tension, consequence, or promise. The cover should create an honest visual question or contrast that invites a click. Do not use the former big-tech cover system, generic abstract anchors, or an unrelated mascot pose.

## Final Response

Report:

- paths to both Markdown files
- path to the filled cover brief, local cover PNG, and uploaded cover URL when generated
- path to the clean WeChat HTML file and preview HTML file when generated
- selected `gzh-design` theme and why
- number of illustrations generated and uploaded
- body-illustration rendering mode; if numbered, report style number/name, blend strength, and whether a numbered style reference image was used
- any blocked steps or credentials needed
