# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background. Flat vector illustration style with bold black outlines and solid color fills. Primary fill color is dark navy blue (#1A2B40). White highlights and outlines on navy elements. Light beige (#F5E6D3) for secondary fills and warm accents. Sparse red (#E74C3C) only for key warnings or results. Orange only for main flow arrows and paths. Light blue for secondary notes. No gradients, no shadows, no paper texture, no complex background, no commercial illustration style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI, no hand-drawn wobbly lines — clean vector lines only.

Recurring IP character required:
YOYO — a compact youthful male character in a fixed 3.2–3.5-head-tall proportion, with an oversized rounded head about 1.35 times shoulder width and short straight legs. Pale skin, short dark hair, large rounded rectangular black-rimmed glasses, dark oval eyes, natural thick short eyebrows, tiny calm mouth, and three short cheek marks on each side. No feminine features, no long hair, no eyelashes. Dark navy baseball cap with a small top button, wide curved brim with a thin white highlight, and a white-bordered navy rectangular front patch showing four Chinese characters "平安喜乐" in a 2x2 grid with one tiny red dot. Dark navy work jacket with white stitching, lapels, centered placket with three light buttons, two symmetrical flap chest pockets with one light button each, dark undershirt, straight dark trousers, and dark low-top lace-up sneakers with white line details. Flat vector style with clean near-black outlines, solid navy fills, and white highlights. Calm, slightly shy expression. Preserve this canonical front/right-side turnaround construction; when a right-facing profile is requested, show the long cap brim, one eyeglass lens and temple arm, one ear, nose bridge and chin profile.
YOYO must perform the core conceptual action in the illustration, not just stand beside the diagram.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：YOYO 在哪里、正在做什么、主要物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Navy blue for main fills and YOYO's outfit. Black for outlines and text. White for background and highlights. Beige for secondary objects. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue for secondary notes or system state. Keep extra colors to 1-2 types max per image.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Invent a fresh visual metaphor for this specific article. It should be clean, creative, and interesting — not childish, not complex, not rigid.
```

## 迭代重生成提示

Nano Banana Pro API 只支持文生图（text-to-image），不支持对已有图片做局部编辑。迭代方式是：在原始提示词末尾追加针对性强调句，然后重新调用 `scripts/generate_image.py`。

常用追加强化句：

**去掉不想要的左上角标题：**

```text
IMPORTANT: Do NOT include any title text, heading text, or label in the top-left corner of the image. The top-left area must remain empty white space.
```

**让 YOYO 更核心：**

```text
IMPORTANT: YOYO must be the central action performer — actively doing the work that explains the core concept, not standing beside or watching the diagram.
```

**纠正风格偏移（太可爱/太商业/太手绘）：**

```text
IMPORTANT: Strict flat vector style. Bold clean black outlines, solid navy fills, no gradients, no shadows, no paper texture, no wobbly hand-drawn lines. Clean and minimal, not cute or commercial.
```

**减少画面元素：**

```text
IMPORTANT: Keep the composition extremely sparse. Only include the essential elements listed above. At least 40% of the canvas must be empty white space.
```

**中文标注纠错：**

```text
IMPORTANT: Chinese text labels must be rendered accurately with correct characters. No garbled or made-up characters. Keep labels short (2-8 characters each).
```

迭代时只追加与问题相关的强化句，不要全部加上，避免提示词过长导致模型忽略关键指令。
