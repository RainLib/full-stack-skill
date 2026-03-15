# 全栈工作流入口

用户通过 `/dev-workflow` 启动全栈开发工作流。编排器按以下 8 阶段顺序执行，每步产出作为下一步输入。

## 阶段与调用方式

| 顺序 | 阶段 | Skill | 调用方式 | 说明 |
|:----:|------|-------|----------|------|
| 1 | 需求分析 | `requirements-analysis` | inline | **与用户对话**，从原型/描述中梳理功能点，模糊处追问 |
| 2 | 技术选型 | `technology-selection` | inline | **先问用户**全栈/仅前端/仅后端，得到答复后再产出选型清单 |
| 3 | 技术评审 | `technical-review` | fork/Explore | 评审架构可行性、API 契约、数据模型、风险 |
| 4 | 程序设计 | `program-design` | inline | **与用户确认**关键假设与方案取舍后再定稿 |
| 5 | 任务拆分 | `task-breakdown` | fork/Plan | 将设计拆为可管理的开发单元 |
| 6 | 单元测试 | `unit-testing` | fork | 按任务单元设计测试用例 |
| 7 | 代码开发 | `code-development` | inline | **与用户确认**范围/方案变更，按测试驱动实现 |
| 8 | 自我验证 | `self-verification` | fork/Explore | 运行测试、集成验证、质量自检 |

Inline 阶段（1、2、4、7）均需与用户对话或确认，不得跳过用户直接生成结果。

## 状态管理

- 所有阶段产出写入 `docs/{current_iteration_id}/`，文件名带 phase id。
- `docs/history.json` 记录当前迭代、各阶段 id 与状态（含创建/更新时间），避免重复生成。
- 无当前迭代时先新建迭代再执行。
- 自我验证未通过时回退到代码开发修复，修复后重新验证。
- 约定见 [docs-convention.md](docs-convention.md)。

## 工具 Skill

- **`history-manager`**：迭代与阶段状态管理 skill，`user-invocable: false`。所有阶段 skill 和编排器通过调用它来读写 `docs/history.json`，而非直接操作文件。内置跨平台 Python 3 脚本（macOS + Windows）。
- 各 skill 的详细说明见各自目录下的 `SKILL.md`；模板在各自 `templates/` 中。
- Frontmatter 规范见 [SKILL_META.md](SKILL_META.md)。
