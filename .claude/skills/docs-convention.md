# 文档与状态管理约定

工作流产出写入 `docs/`，状态与历史由 `docs/history.json` 管理。跨平台操作通过 `history-manager` skill（内置 Python 3 脚本）。

## 1. history.json 结构

- **schema_version**：`"1.0"`。
- **current_iteration_id**：当前进行中的迭代 id（如 `iter-001`）；新建迭代时生成并写入。
- **iterations**：数组，每项为一次迭代：
  - **id**：迭代 id，与目录 `docs/{id}/` 对应。
  - **state**：当前处于的阶段（见下方状态机）。
  - **phases**：各阶段对应 id（用于文件名、避免重复生成）：
    - `requirements_id`
    - `technology_selection_id`
    - `technical_review_id`
    - `program_design_id`
    - `task_breakdown_id`
    - `unit_testing_id`
    - `code_development_id`
    - `self_verification_id`
  - **created_at**、**updated_at**：ISO 8601 时间。
- **created_at** / **last_updated**：文件级别的创建与最后更新时间。

## 2. 状态机

```
requirements → technology_selection → technical_review → program_design
→ task_breakdown → unit_testing → code_development → self_verification → done
```

- `self_verification` 未通过时不前进，保持当前状态，待修复后重试。
- `done` 为终态。

有效 state 值：`requirements`、`technology_selection`、`technical_review`、`program_design`、`task_breakdown`、`unit_testing`、`code_development`、`self_verification`、`done`。

## 3. 迭代与阶段 id 生成

- **迭代 id**：`iter-` + 三位数字，如 `iter-001`。新迭代取当前最大编号 +1。
- **阶段 id**：`{阶段缩写}-` + 三位数字，在同一迭代内唯一：
  - 需求分析：`req-001`
  - 技术选型：`ts-001`
  - 技术评审：`tr-001`
  - 程序设计：`pd-001`
  - 任务拆分：`tb-001`
  - 单元测试：`ut-001`
  - 代码开发：`cd-001`
  - 自我验证：`sv-001`

## 4. 避免重复生成

- 执行某阶段前，先读 `history.json`，取 `current_iteration_id` 及该迭代的 `phases.xxx_id`。
- 若该阶段已有 `xxx_id` 且 `docs/{iteration_id}/{阶段名}-{xxx_id}.md` 已存在，则**不重新生成**，直接使用已有文件作为输入进入下一阶段；除非用户明确要求「重新做某阶段」。
- 若该阶段尚未有 id，则生成新 phase id、写入产出文件、更新 `history.json`。

## 5. 产出写入位置

- 根目录：项目下的 `docs/`（与 `.claude` 平级）。
- 当前迭代目录：`docs/{current_iteration_id}/`；若不存在则先创建。
- 文件名：`{阶段名}-{phase_id}.md`，例如 `requirements-req-001.md`。

| 阶段 | 文件名格式 |
|------|-----------|
| 需求分析 | `requirements-{req-xxx}.md` |
| 技术选型 | `technology-selection-{ts-xxx}.md` |
| 技术评审 | `technical-review-{tr-xxx}.md` |
| 程序设计 | `program-design-{pd-xxx}.md` |
| 任务拆分 | `task-breakdown-{tb-xxx}.md` |
| 单元测试 | `unit-testing-{ut-xxx}.md` |
| 代码开发 | `code-development-{cd-xxx}.md` |
| 自我验证 | `self-verification-{sv-xxx}.md` |

## 6. 每次更新 history 时

- 更新该迭代的 `updated_at`。
- 更新全局 `last_updated`。
- 若新建迭代：生成新迭代 id、创建目录 `docs/{iter-id}/`、push 迭代记录、设置 `current_iteration_id`。

## 7. history-manager Skill

`history-manager` 是一个 `user-invocable: false` 的工具 skill，所有阶段 skill 和编排器通过调用它来管理 `docs/history.json`，而非直接读写文件。

内置跨平台（macOS + Windows）Python 3 脚本。支持的命令：

- `init` — 初始化 history.json
- `new-iter` — 创建新迭代
- `set-phase <phase> <phase_id>` — 记录阶段完成并推进状态
- `get-phase <phase>` — 获取当前阶段 id
- `check-file <phase> <phase_id>` — 检查阶段文档是否存在
- `status` — 输出当前迭代状态

详见 `history-manager/SKILL.md`。
