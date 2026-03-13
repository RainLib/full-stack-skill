我需要设计一个skills的工作流程.

需求分析-功能点梳理和细节要求
技术选型-询问用户需要全栈开发,还是仅前端开发, 还是仅后端开发, 然后分别进入对应的 技术选择
程序设计-根据技术选型, 设计程序的结构和流程和工程结构目录要求等
单元测试-根据程序设计, 设计单元测试的用例和预期结果
代码开发-根据单元测试, 开发代码


## 按照以上要求进行设计
1. 不同类型内容需要有参考的模板
2. 需要相应细节的引导内容
3. skill.md 尽量轻量

---

## 已实现对应目录（与本文件一致）

| 阶段     | 技能目录                 | 模板与引导 |
|----------|--------------------------|------------|
| 需求分析 | `requirements-analysis/` | `templates/requirements-template.md` |
| 技术选型 | `technology-selection/`  | `templates/fullstack.md`、`frontend-only.md`、`backend-only.md` |
| 程序设计 | `program-design/`       | `templates/design-template.md` |
| 单元测试 | `unit-testing/`         | `templates/test-case-template.md` |
| 代码开发 | `code-development/`     | `templates/development-checklist.md` |

入口与顺序见 `CLAUDE.md`，总览见 `README.md`。

## 文档与状态管理（已实现）

- **规范化文档**：产出统一放在 **`docs/`** 下，按 **迭代 + id** 组织：`docs/{iteration_id}/`（如 `docs/iter-001/`），各阶段文件名为 `{阶段名}-{phase_id}.md`，阶段 id 由 history 记录，避免重复生成。
- **历史与状态**：**`docs/history.json`** 记录当前迭代、各迭代状态（含 `created_at`、`updated_at`）、各阶段 id；约定与字段说明见 **`.claude/skills/docs-convention.md`**。
- 每个阶段均有对应 phase id（`requirements_id`、`technology_selection_id`、`program_design_id`、`unit_testing_id`、`code_development_id`），便于追溯与防重复生成。
