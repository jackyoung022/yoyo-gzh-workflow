---
name: yoyo-illustrations
description: 生成 YOYO 风格的中文正文配图。用于用户要求为中文文章、帖子、博客、Notion 文档、工作流文档、方法论、流程、结构、状态、隐喻或观点生成插图。使用 YOYO IP（深蓝扁平矢量、戴眼镜鸭舌帽的年轻人）、纯白背景、有限色板、简洁但有创意的视觉风格。
---

# YOYO 中文正文配图

## 核心定位

为中文文章设计和生成 16:9 横版正文配图。目标不是做商业插画、PPT 信息图或卡通海报，而是把文章里的关键判断、流程、结构、状态或隐喻，变成一张干净、有创意、有 YOYO 角色参与的扁平矢量解释图。

默认视觉 IP 是"YOYO"：短身、大头比例的年轻男生，戴圆框眼镜和深蓝鸭舌帽，穿深蓝工装夹克、深色长裤与运动鞋；表情平和略带害羞，认真做一件和概念相关的事。外观以正面与右侧面设定资产为唯一基准，YOYO 必须参与画面的核心动作，不能只是站在旁边当装饰。

## API Key 配置

本 skill 使用 Google Nano Banana Pro API 生图。用户需要先手动配置 API Key。

两种方式任选其一：

**方式 1：环境变量**

```bash
export GOOGLE_API_KEY="your-api-key-here"
```
建议写入 `~/.zshrc` 或 `~/.bashrc` 使其持久生效。

**方式 2：Key 文件**
```bash
mkdir -p ~/.config/yoyo-illustrations
echo "your-api-key-here" > ~/.config/yoyo-illustrations/api_key
```

脚本会按优先级查找：环境变量 → key 文件。未找到 Key 时会报错并提示配置方式。

## 先读这些参考

按任务需要读取，不要一次塞满上下文：

- `references/style-dna.md`：风格 DNA、颜色、文字、禁忌。
- `references/yoyo-ip.md`：YOYO IP 的形象、性格、动作库和禁忌。
- `references/composition-patterns.md`：结构类型、原创隐喻方法和反复刻规则。
- `references/prompt-template.md`：单张生图提示词模板。
- `references/qa-checklist.md`：生成后检查和迭代规则。
- `assets/yoyo-ip-front.png`：YOYO 正面标准设定图；用于锁定头身比例、正面五官、服装和配色。
- `assets/yoyo-ip-side-right.png`：YOYO 右侧面标准设定图；用于锁定帽檐、眼镜腿、耳朵、鼻梁与服装侧面轮廓。
- `assets/yoyo-reference.png`：旧场景参考，仅用于饮品道具与线条风格补充；不得覆盖正侧面标准设定。

## 工作流

### 1. 消化正文

先读用户给的正文、链接、Notion 页面、Markdown 文件或截图内容。提炼：

- 核心观点是什么
- 哪些段落承担认知转折
- 哪些内容适合用图解释
- 哪些地方只适合文字，不需要图

不要平均配图。优先选择"认知锚点"，例如：核心判断、两个断点、输入输出闭环、分流、前后对比、一鱼多吃、承接路径、常见坑、角色状态变化。

### 2. 先出配图策略

如果用户只是说"分析怎么配图 / 思考哪些地方需要配图"，先给 shot list。每张图写清楚：

- 放在哪个段落后
- 图的主题
- 核心意思
- 结构类型
- YOYO 在图里做什么
- 建议元素
- 建议中文标注词

默认 4-8 张。文章很短时 1-3 张；长文也不要轻易超过 9 张。够用就好，避免把正文做成画册。

### 3. 单张生成

如果用户明确要求"生成 / 输出 / 做图 / 帮我生成"，不要停下来等确认；用 `scripts/generate_image.py` 每张单独生成。不要把多张图拼在一张里。

生成命令：

```bash
python3 scripts/generate_image.py \
  --prompt "$(cat <<'PROMPT_EOF'
这里放入完整的生图提示词
PROMPT_EOF
)" \
  --output "assets/<article-slug>-illustrations/01-topic-name.png"
```

脚本参数：
- `--prompt`（必选）：生图提示词，按 `references/prompt-template.md` 模板组装。
- `--output`（必选）：输出 PNG 路径。
- `--reference`（可选）：角色参考图路径，默认自动使用 `assets/yoyo-ip-front.png`。需要明确侧面姿态时，传入 `assets/yoyo-ip-side-right.png`；上传参考图能更好地锁定 YOYO 形象。
- `--no-reference`（可选）：禁用参考图上传。
- `--model`（可选）：覆盖模型名，默认 `gemini-3-pro-image`。
- `--image-size`（可选）：`1K` / `2K` / `4K`，默认 `2K`。
- `--aspect-ratio`（可选）：宽高比，默认 `16:9`。
- `--base-url`（可选）：覆盖 API 地址（用于代理或第三方中转）。

脚本零依赖（只用 Python 3 标准库），不需要 pip install。

每张图只讲一个核心结构。提示词必须包含：

- 16:9 横版中文正文配图
- 纯白背景
- 深蓝扁平矢量风格，粗黑描边
- 有限色板：深蓝为主、白色高光、米色和少量红色点缀
- 大量留白
- YOYO 作为核心动作主体
- 禁止 PPT、商业插画、幼稚可爱、复杂架构、左上角类型标题

不要复刻过往案例。每次都要从当前文章重新发明一个有趣但成立的隐喻。

### 4. 检查与迭代

生成后检查 `references/qa-checklist.md`。如果出现以下问题，调整提示词后**重新生成**（Nano Banana Pro API 不支持局部编辑，只能整张重新生成）：

- YOYO 只是装饰
- 画面太满
- 太像流程图/PPT
- 中文太多或错字严重
- 左上角出现标题
- 画风偏离深蓝矢量风格
- 背景不是干净白底

迭代策略：在提示词中加强缺失约束（例如强调 "YOYO must be the central action performer" 或 "limited color palette, navy blue dominant"），然后重新调用脚本。

### 5. 保存交付

如果用户在 workspace 内工作，把最终图复制到：

```text
assets/<article-slug>-illustrations/
```

按顺序命名：

```text
01-topic-name.png
02-topic-name.png
```

保留原始生成文件，不要覆盖已有资产，除非用户明确要求替换。

## 输出口径

生成前的策略输出要短而准。生成后的交付要包含：

- 生成了几张
- 每张图的用途
- 保存路径
- 哪些图最稳，哪些图是可选

不要长篇解释风格理论；让图自己说话。
