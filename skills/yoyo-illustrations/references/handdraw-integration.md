# Handdraw 编号画风集成

仅在用户指定 `001`–`279` 风格编号时读取本文件。这里把 handdraw 包作为编号解析器和风格资产库，不完整调用该 Skill：不要执行它的会话初始化、画廊打开、纯图状态行、四段式提示词输出或 `article-illustration-planner` 路由。文章内容、构图、角色和生成流程始终由 YOYO v2 负责。

## 依赖定位

依赖完整安装的 `handdraw-style-prompter` 仓库根目录。根目录必须同时包含：

- `SKILL.md`
- `images/individual/`
- `skills/handdraw-style-prompter/references/styles.json`
- `skills/handdraw-style-prompter/scripts/resolve_reference.py`

从当前可用技能目录解析实际安装路径；不要假设工作区内存在副本。若入口指向嵌套的 operational Skill，从该位置逐级向上查找，直到同一目录同时包含 `images/individual/` 和 `skills/handdraw-style-prompter/scripts/resolve_reference.py`，该目录才是包根。若找不到，报告依赖不完整，不要编造或替换参考图。

## 解析步骤

1. 将用户输入标准化为三位编号，例如 `10` 转为 `010`。
2. 在 handdraw 包根目录运行：

   ```bash
   python3 skills/handdraw-style-prompter/scripts/resolve_reference.py \
     --model gpt-image-2 \
     --style 010
   ```

3. 从 `skills/handdraw-style-prompter/references/styles.json` 中读取同编号记录，只使用真实字段：

   - `generation_name`
   - `reference`
   - `traits`

4. 以解析器 JSON 为准使用：

   - `activation_source`
   - `prompt_traits`
   - `use_reference_image`
   - `reference_path`

5. 编号无效、记录缺失或参考图缺失时停止该编号融合，并请用户选择有效编号；不要猜测名称或特征。

## 提示词构造

始终写入：

- `Handdraw style: #<number> · <generation_name>`
- `Indexed reference label: <reference>`
- `Blend strength: safe | balanced | full`

仅当解析器返回非空 `prompt_traits` 时，把这些正向、可见的特征加入提示词。不要机械复制原始 `traits`，不要加入包含“避免、不要、不准、禁止”的片段。

根据 `references/style-dna.md` 的融合强度过滤冲突特征：

- `safe`：只保留形状语言、轮廓节奏、留白方式、视觉气质和幽默机制。
- `balanced`：在 safe 基础上允许局部线条、笔触、媒介、材质和少量配色倾向。
- `full`：允许完整媒介与配色倾向，但仍不得覆盖 YOYO 身份、用户内容和正文结构。

所有强度都必须删除会改变 YOYO 身份的特征，包括但不限于：新的头身比例、眼睛大小或形状、脸型、五官、发型、服装、年龄、性别、性格、表情机制或肢体结构。只保留渲染语言；例如 #217 的“夸张头身比例、富有表现力的大眼”必须删除，而“风格化 3D、独特剪影、局部触感材质”可以按强度保留。

## 参考图角色隔离

YOYO 参考图始终排在第一张。解析器要求风格参考图时，编号参考图排在第二张。对内置 imagegen 使用 `referenced_image_paths`：

```text
[
  "<yoyo-skill>/assets/yoyo-ip-front.png",
  "<handdraw-root>/images/individual/.../<number>.webp"
]
```

在提示词中明确：

```text
Input image 1 is the canonical YOYO character reference. Preserve only the character's identity, proportions, face, glasses, cap patch, work jacket, clothing construction, and calm personality. Do not copy its pose or scene unless explicitly requested.

Input image 2 is a rendering-style reference only. Extract only linework, brushwork, medium, material texture, color tendencies, shape language, and overall visual rhythm. Do not copy or continue any subject, person, animal, clothing, prop, action, pose, setting, background, composition, layout, text, or story from it. The user's theme and the YOYO specification are the sole sources for content and character identity.
```

如果解析器不需要编号参考图，只传 YOYO 角色参考图；不要为了“更像”而强制添加风格图。

## 优先级

用户明确内容与文字 > YOYO 身份 > 内容隐喻与结构 > 正文配图约束 > 编号画风。

当编号画风与 YOYO 硬约束冲突时，不要把冲突原样写进提示词：先按融合强度过滤。若 `full` 导致角色识别失败，自动降级为 `balanced` 后重生成一次，并在交付中说明降级。
