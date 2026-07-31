# Output Contract

Use this contract when saving final article drafts.

## Files

Create exactly two user-facing Markdown files unless the user asks for more:

- `<slug>-wechat.md`
- `<slug>-blog.md`

Use the active workspace's `outputs/` directory when available.

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

Use OSS URLs in final Markdown when upload succeeded. Use local paths only when upload failed or the user explicitly asks for local-only drafts.

Use concise alt text or captions that describe the idea, not the visual style.

## Final Response

Report:

- paths to both Markdown files
- path to the clean WeChat HTML file and preview HTML file when generated
- selected `gzh-design` theme and why
- number of illustrations generated and uploaded
- any blocked steps or credentials needed
