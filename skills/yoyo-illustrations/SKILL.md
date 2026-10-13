---
name: yoyo-illustrations
description: 为中文文章规划并生成 16:9 YOYO IP 正文配图，可选融合 handdraw-style-prompter 的 001–279 编号画风。使用内置 imagegen 生图，适用于文章、帖子、博客、Notion 文档、工作流、方法论、流程、结构、状态、隐喻或观点配图。
---

# YOYO 中文正文配图 v2

## 定位

把中文文章中的关键判断、流程、结构、状态或隐喻，变成干净、有创意、有 YOYO 参与核心动作的 16:9 横版正文配图。

YOYO 是固定视觉 IP：短身、大头比例的年轻男生，戴圆框眼镜和深蓝鸭舌帽，穿深蓝工装夹克、深色长裤与运动鞋，表情平和略带害羞。正面与右侧面设定图是角色身份的唯一视觉基准。无论是否融合编号画风，YOYO 的人物结构、服装识别点、性格和核心动作地位都不能被覆盖。

默认使用 YOYO 原生深蓝扁平矢量风。用户提供 `001`–`279` 风格编号时，以 YOYO 为内容与角色主层，以 `handdraw-style-prompter` 为可选渲染层。

## 生成方式

使用 Codex 内置 `imagegen` 能力。不要要求 API Key，不要调用本地 API 脚本，也不要因为需要参考图而切换到 CLI。

内置 `imagegen` 不暴露模型选择参数，因此不要伪造 `--model` 参数或声称已手动锁定底层模型。编号画风的激活判断固定按用户指定的 `gpt-image-2` 配置解析；实际生图口径只报告“使用内置 imagegen”。

- 用户只要求分析或配图策略时，输出 shot list，不生图。
- 用户明确要求生成、输出、做图、预览或渲染时，直接调用内置 `imagegen`；每张图单独调用一次。
- 多张图使用多次独立调用，不把不同主题拼成一张。
- 如果内置生图不可用或失败，说明失败，不要静默切换 API/CLI。
- 项目内使用的成图要复制到工作区的 `assets/<article-slug>-illustrations/`；预览图可直接内联展示。

## 按需读取

- `references/style-dna.md`：原生风格与融合强度边界。
- `references/yoyo-ip.md`：角色形象、性格、动作和禁忌。
- `references/composition-patterns.md`：结构类型和原创隐喻方法。
- `references/prompt-template.md`：单张图的内置 imagegen 提示词模板。
- `references/handdraw-integration.md`：用户指定编号画风时的解析、过滤、双参考图和优先级规则。
- `references/qa-checklist.md`：生成后的角色、内容和风格检查。
- `assets/yoyo-ip-front.png`：默认角色参考图。
- `assets/yoyo-ip-side-right.png`：明确右侧面动作时的角色参考图。
- `assets/yoyo-reference.png`：仅补充饮品道具和原生线条感，不得覆盖正侧面设定。

## 输入

接收正文、文章链接、Markdown、截图或单张配图主题。可选输入：

- `风格：010` 或任意 `001`–`279` 编号。
- `版式：SC-008` 等布局编号。布局编号指定构图与文字槽位，不等同于 `001`–`279` 画风编号；从 handdraw-style-prompter 的 `references/layouts.json` 和对应 `references/layouts/<编号>.md` 核对实际含义。
- `融合：safe | balanced | full`，中文别名为 `保守 | 平衡 | 完整`。
- 角色朝向、必须出现的中文标注、输出数量和保存位置。

没有指定融合强度时：未选编号画风则使用原生模式；选了编号画风则默认 `balanced`。

## 工作流

### 1. 消化正文

提炼核心观点、认知转折和适合视觉化的内容。不要平均配图；优先选择核心判断、断点、输入输出闭环、分流、前后对比、承接路径、常见坑和角色状态变化。

### 2. 先定配图策略

用户只要求分析时，给出简短 shot list。每张写清：插入位置、主题、核心意思、结构类型、YOYO 的核心动作、建议元素和中文标注。默认 4–8 张；短文 1–3 张；一般不超过 9 张。

### 3. 解析编号画风

仅在用户指定编号时读取 `references/handdraw-integration.md` 并执行其中的解析规则。编号必须来自已安装的 `handdraw-style-prompter`，不得猜测名称、风格特征或参考图。

用户指定 `SC-008` 一类布局编号时，从布局库读取构图规则，适配正文要求的 16:9 和 YOYO 身份。布局参考图只提供构图、留白及可兼容的表面处理，不得复制其中的人物、道具、文案或故事；用户要求无图中文字时，删除该布局的文字槽位，不自行补文案。

### 4. 组装单张提示词

读取 `references/style-dna.md`、`references/yoyo-ip.md`、`references/composition-patterns.md` 和 `references/prompt-template.md`。一张图只表达一个核心结构；每次从当前文章重新设计隐喻，不复刻旧案例。

提示词优先级从高到低：

1. 用户明确内容与文字要求。
2. YOYO 身份、服装和动作主体地位。
3. 正文结构与原创隐喻。
4. 16:9、留白、少量中文标注等正文配图约束。
5. 编号画风及融合强度。

低优先级画风不能改变高优先级内容、人物身份、文字或结构。

### 5. 使用 imagegen 生成

使用内置 `imagegen`，新图的用例归类为 `stylized-concept`。

- 始终传入一张 YOYO 角色参考图。默认正面；明确右侧面动作时使用右侧面设定图。
- 解析器要求编号风格参考图时，同时传入角色参考图和风格参考图，并在提示词中分别标注两张图的角色。
- 两张图都是本地文件时，通过 `referenced_image_paths` 一次传入，角色图在前、风格图在后。
- 角色图只锁定人物身份；风格图只提供线条、笔触、媒介、材质、色彩倾向和视觉语言，禁止复制其中的主体、动作、场景、构图、布局、文字或故事。

### 6. 检查与迭代

读取 `references/qa-checklist.md`。先检查 YOYO 身份和内容表达，再检查编号画风命中度。失败时只针对一个主要问题修改提示词并重新生成；不要一次追加全部强化句。

### 7. 保存交付

工作区内最终图保存到：

```text
assets/<article-slug>-illustrations/01-topic-name.png
assets/<article-slug>-illustrations/02-topic-name.png
```

不覆盖已有资产，除非用户明确要求替换。否则使用递增或 `-v2` 文件名。

## 输出

生成前的策略要短而准。生成后说明：

- 生成数量与每张用途。
- 使用的 YOYO 角色参考图。
- 是否使用编号画风、编号、名称和融合强度。
- 是否使用编号风格参考图。
- 最终保存路径；预览任务则直接展示图片。

不要长篇解释风格理论。
