# 内置 imagegen 提示词模板

每张图单独组装。删掉未使用的可选段落，不要把变量占位符发送给 imagegen。

```text
Use case: stylized-concept
Asset type: 16:9 horizontal illustration embedded in a Chinese article

Primary request:
Create one standalone illustration for this article theme: {正文配图主题}

Core idea:
{这张图只表达的一个核心判断、结构、状态或隐喻}

Composition:
{YOYO 在哪里、正在做什么、主要物件是什么、信息或动作如何流动}

Recurring character:
YOYO must perform the core conceptual action, not stand beside or watch the structure. Preserve the canonical YOYO identity from input image 1: a compact youthful male character in a fixed 3.2–3.5-head-tall proportion; oversized rounded head; pale skin; short dark hair; large rounded rectangular black-rimmed glasses; calm small mouth; three short cheek marks on each side; dark navy baseball cap with a white-bordered navy patch showing the four Chinese characters "平安喜乐" in a 2x2 grid and one tiny red dot; dark navy work jacket with white stitching, lapels, three light front buttons and two symmetrical flap chest pockets; dark undershirt, straight dark trousers, and dark low-top lace-up sneakers. Calm, slightly shy expression. Do not copy the reference image's pose or scene unless requested.

Structure type:
{Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Suggested elements:
{只列必要的 1–4 个元素}

Chinese labels (verbatim):
{0–8 个短标注；没有则写 none}

Rendering mode:
{native-yoyo 或 handdraw blend 段落}

Composition constraints:
One image explains one idea. Keep the active subject around 40%–60% of the canvas and preserve at least 35% negative space. No title or type label in the top-left. Do not write the structure type in the image. Keep Chinese labels sparse and legible. Avoid PPT, course-slide, formal-flowchart, dense-explainer, commercial-mascot and childish-poster aesthetics. Invent a fresh physical metaphor for this article.

Input image roles:
Input image 1 is the canonical YOYO character reference. Use it only to preserve character identity, proportions, face, glasses, cap patch, clothing construction, palette anchors, and calm personality.
{仅当传入第二张风格图时加入 Input image 2 隔离声明}
```

## native-yoyo 段落

```text
Native YOYO visual DNA. Pure white background. Flat vector illustration with clean near-black outlines and solid fills. Dark navy #1A2B40 is dominant; white highlights; light beige #F5E6D3 for secondary objects; sparse red #E74C3C only for key warnings or results; orange only for the main path; light blue only for secondary state. No gradients, shadows, paper texture, noise, realistic UI, complex background or wobbly hand-drawn lines. Use no more than 1–2 accent colors beyond navy, black and white.
```

## handdraw blend 段落

先按 `handdraw-integration.md` 解析真实字段并按融合强度过滤，再填入：

```text
Handdraw style: #{编号} · {generation_name}
Indexed reference label: {reference}
Blend strength: {safe | balanced | full}
Resolved positive rendering traits: {解析器返回并经过融合过滤的 prompt_traits；空则省略本行}
Blend behavior: {从 style-dna.md 对应强度提炼成 1–3 句，不加入冲突描述}
```

解析器要求风格参考图时，追加：

```text
Input image 2 is a rendering-style reference only. Extract only its linework, brushwork, medium, material texture, color tendencies, shape language, and overall visual rhythm. Do not use, copy, or continue any subject, person, animal, clothing, prop, action, pose, setting, background, composition, layout, text, or story from it. The user's theme and the YOYO specification are the sole sources for content and character identity.
```

## 针对性重生成句

一次只追加最相关的一条：

- 角色漂移：`Preserve YOYO's canonical face, proportions, cap patch, glasses, work jacket construction and calm personality from input image 1. Do not restyle away these identity anchors.`
- YOYO 只是装饰：`YOYO must be the central action performer whose physical action makes the core idea understandable.`
- 风格图污染内容：`Use input image 2 for rendering style only. Remove every subject, prop, scene, layout and text borrowed from it.`
- 风格不明显：`Increase the resolved linework, shape language and material qualities of handdraw style #{编号}, while preserving YOYO's identity and the requested content.`
- 画面太满：`Keep only the named essential elements and reserve at least 40% blank space.`
- 中文错误：`Render only the quoted Chinese labels, verbatim, with no additional text.`
