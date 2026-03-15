# 规范化文档目录

本目录存放按**迭代**组织的工作流产出，并与 `history.json` 配合做状态管理与历史追溯。

## 目录约定

- **迭代目录**：`docs/{iteration_id}/`，例如 `docs/iter-001/`。
- **当前迭代**：由 `history.json` 的 `current_iteration_id` 指明。
- **阶段产出**：每阶段产出写入当前迭代目录，文件名带**阶段 id**，避免重复生成。

## 8 阶段产出文件

| 阶段 | 阶段 id 字段 | 文件名格式 |
|------|-------------|-----------|
| 需求分析 | `requirements_id` | `requirements-{id}.md` |
| 技术选型 | `technology_selection_id` | `technology-selection-{id}.md` |
| 技术评审 | `technical_review_id` | `technical-review-{id}.md` |
| 程序设计 | `program_design_id` | `program-design-{id}.md` |
| 任务拆分 | `task_breakdown_id` | `task-breakdown-{id}.md` |
| 单元测试 | `unit_testing_id` | `unit-testing-{id}.md` |
| 代码开发 | `code_development_id` | `code-development-{id}.md` |
| 自我验证 | `self_verification_id` | `self-verification-{id}.md` |

若某阶段已有 id 且对应文件已存在，则不再重新生成该阶段产出，除非用户明确要求。

## history.json

见 [history.json](./history.json)。记录当前迭代、各迭代状态、各阶段 id、创建与更新时间。

[history.schema.json](./history.schema.json) 为 JSON Schema，便于校验与工具解析。

状态管理说明见 [.claude/skills/docs-convention.md](../.claude/skills/docs-convention.md)。
