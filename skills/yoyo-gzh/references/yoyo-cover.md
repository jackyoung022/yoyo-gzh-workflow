# YOYO WeChat Cover

Read this reference after the final article title and core thesis are stable. It defines the default cover workflow for a full `yoyo-gzh` publication package.

The cover must use the canonical YOYO IP, retain the article title as visible text, and turn the article's central tension into one simple visual action. It must not use the former minimalist big-tech system, an abstract logo-like anchor, a generic technology gradient, or a mascot pose unrelated to the article.

## Read the YOYO Source of Truth

Before designing the cover, load these resources from the `yoyo-illustrations` companion skill:

- `references/yoyo-ip.md` for the canonical character construction and forbidden changes
- `references/style-dna.md` for the restrained navy vector language and limited palette
- `assets/yoyo-ip-front.png` and `assets/yoyo-ip-side-right.png` as character references for generation

The cover may adapt the body-illustration style to a wide cover, but it must preserve YOYO's fixed face, glasses, cap, clothing, proportions, and calm personality.

## Fill the Cover Brief

Infer these fields from the final article and any user preferences. Preserve an exact user-supplied value. Ask only when a missing choice would materially change the result.

```markdown
# YOYO Cover Brief

Article thesis: <one sentence stating the article's answer or judgment>

Audience promise: <what useful insight, tension, or consequence makes this worth opening>

Exact title text: <the final article title, unchanged unless the user explicitly approves another cover title>

Title line breaks: <one to three deliberate lines using the exact title text>

Aspect ratio: <ratio>

Layout: <title left / YOYO right by default>

YOYO action: <one concrete action that embodies the article's core tension, consequence, or promise>

Article-specific object: <one primary object or compact scene element tied to the article>

Click-driving visual question: <the honest unresolved moment, contrast, or consequence shown visually>

Palette notes: <restrained color guidance within the YOYO visual system>

Reference assets: <canonical YOYO front and right-side images>

OSS URL: <fill after upload>
```

Save it as `outputs/<slug>-cover-brief.md`.

### Inference Defaults

- **Article thesis:** use the direct answer established in the opening, not a vague theme label.
- **Audience promise:** identify the insight, practical payoff, surprising consequence, or decision the reader gains from the article.
- **Exact title text:** use the final article title verbatim. Do not silently shorten, rewrite, or replace it with clickbait. If it is too long for a legible cover, first improve line breaks; use alternate cover text only when the user explicitly asks for or approves it.
- **Title line breaks:** use one to three lines, preserving the exact character order and punctuation.
- **Aspect ratio:** default to `5:2` for a WeChat cover. Use the user's requested ratio when supplied.
- **Layout:** default to title on the left and YOYO on the right. Mirror the sides only when the user requests it or a supplied reference requires it. Never use a stacked title-above-character composition.
- **YOYO action:** turn the thesis into one physical verb such as pulling, sorting, repairing, holding back, opening, connecting, weighing, or filtering.
- **Article-specific object:** choose one recognizable object or compact scene element derived from the article. Avoid decorative gadgets, fake logos, and generic AI circuitry.
- **Click-driving visual question:** create a truthful moment of tension or incomplete action that the title resolves, such as a choice about to be made, a broken link being repaired, an overloaded object about to tip, or two unequal outcomes being weighed. The cover may be intriguing, but it must not promise something the article does not deliver.

## Composition Contract

Use a strong horizontal two-zone composition:

- Reserve the left zone for title text and the right zone for YOYO by default.
- Keep text and character in separate, non-overlapping safe areas. No letter, punctuation mark, prop, arm, hat, or motion line may cover or pass behind the other zone's primary content.
- YOYO's visible figure, measured by its character bounding box, must span about 25%-30% of the full canvas width. Do not count nearby props or empty space toward this share. Do not shrink YOYO into a corner and do not enlarge the character until it competes with the title.
- Give the title enough width and whitespace to remain legible in a small WeChat thumbnail.
- Let one article-specific object connect YOYO's action to the title's idea. Use no more than two supporting elements.
- Keep the background clean and quiet. Use pure white by default; a very light neutral field is acceptable when it improves contrast.
- Preserve clear margins on all edges, especially around the title and YOYO's cap, hands, and feet.

The result should be understood in this order: title first, YOYO's action second, article-specific tension third.

### Title Text

- Render only the exact approved article title.
- Do not add a subtitle, date, category label, English microcopy, author, signature, or slogan.
- Use large, heavy, modern Chinese sans-serif lettering with high contrast against the background.
- Create hierarchy through size, weight, deliberate line breaks, and whitespace rather than outlines, extrusion, glow, or exaggerated shadows.
- Check every Chinese character and punctuation mark against the approved title.

### YOYO and Article Relevance

- Preserve YOYO's canonical glasses, dark navy cap with the `平安喜乐` patch, dark navy work jacket, short proportions, and calm expression.
- YOYO must perform the action that carries the article idea. Do not use a waving, pointing, standing, or thinking pose unless that action itself is central to the article.
- The object, gesture, and spatial relationship must come from the article's thesis or strongest consequence, not merely its industry category.
- Favor a single, instantly readable visual metaphor over a collage, flowchart, UI, or busy scene.
- Use curiosity through a meaningful contrast or unresolved action, never through shock, deception, exaggerated emotion, or unrelated spectacle.

## Generate With Imagegen

Use the built-in `imagegen` mode with the two canonical YOYO reference assets. Generate a new image rather than modifying an unrelated cover.

The prompt must state:

- intended use as a WeChat cover
- exact aspect ratio and native composition for that ratio
- exact title text and line breaks, with a ban on all additional text
- title-left / YOYO-right two-zone layout unless an approved mirrored layout applies
- strict non-overlap between the text safe area and YOYO safe area
- YOYO's visible character bounding box at about 25%-30% of canvas width, excluding props and empty space
- the article thesis, audience promise, YOYO action, article-specific object, and click-driving visual question
- canonical YOYO appearance and the supplied reference images as the identity source of truth
- clean background, restrained navy vector palette, sparse supporting elements, and generous whitespace
- prohibition on generic big-tech gradients, fake logos, decorative circuitry, mascot poses, dense UI, collage, and unrelated spectacle

Save the accepted image as `assets/<slug>-cover.png`. If that name exists and the user did not explicitly request replacement, use a versioned sibling such as `assets/<slug>-cover-v2.png`.

## Inspect and Retry

Check the generated cover before acceptance:

- the aspect ratio is within 0.5 percent of the requested ratio
- every Chinese character and punctuation mark matches the approved title; no extra text appears
- the layout is clearly left-right, with title on the left and YOYO on the right unless a mirrored layout was approved
- title, YOYO, props, and motion lines do not overlap or obscure one another
- YOYO's visible character bounding box occupies about 25%-30% of canvas width, excluding props and empty space
- YOYO matches the canonical IP and is not reduced to a decorative mascot pose
- YOYO's action and the main object visibly relate to the article's core thesis or consequence
- the cover creates a clear, truthful reason to click without misleading the reader
- the background remains clean, the title stays legible at thumbnail size, and the scene is not crowded
- no former big-tech treatment, fake logo, generic AI circuitry, dense UI, collage, or decorative clutter appears

For a failed check, make one targeted prompt correction and regenerate. Allow at most two targeted retries after the first generation. If title accuracy, character fidelity, proportion, relevance, or layout still fails, keep the best local candidate, report the exact issue, and do not call it publication-ready.

Upload the accepted cover with `aliyun-oss-upload`. Record the returned public URL in the brief and report both the local path and URL in the final response.
