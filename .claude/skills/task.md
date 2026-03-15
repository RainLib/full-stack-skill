# 全栈 Skills 工作流设计

## 工作流定义（8 阶段）

1. **需求分析**：从产品原型/需求文档中梳理功能点与细节要求
2. **技术选型**：询问用户全栈/仅前端/仅后端，进入对应技术选择
3. **技术评审**：评审架构可行性、定义 API 契约、数据模型、识别风险
4. **程序设计**：根据选型与评审设计程序结构、流程和工程目录
5. **任务拆分**：将设计拆分为可管理的开发节奏（批次、依赖、优先级）
6. **单元测试**：根据设计与任务拆分设计测试用例和预期结果
7. **代码开发**：根据单元测试按任务顺序开发代码
8. **自我验证**：运行全量测试、集成验证、代码质量自检

## 设计要求

1. 不同阶段有参考模板（各 `templates/` 目录）
2. 需要相应细节的引导内容（各 SKILL.md 中的执行要点与细节引导）
3. SKILL.md 尽量轻量（细节放在 templates/ 中）
4. 需要对话的阶段 inline 执行，只读/生成类阶段用 `context: fork` 子 agent
5. 编排入口 `/dev-workflow` 由用户手动触发，各阶段对用户隐藏
6. 状态管理与文档规范化到 `docs/` 目录，按迭代+id 组织
7. 脚本兼容 macOS 和 Windows（使用 Python 3）

## 已实现对应目录

| 阶段 | 技能目录 | 模板 | 调用方式 |
|------|----------|------|----------|
| 编排入口 | `dev-workflow/` | - | 用户 `/dev-workflow` |
| 需求分析 | `requirements-analysis/` | `requirements-template.md` | inline |
| 技术选型 | `technology-selection/` | `fullstack.md`、`frontend-only.md`、`backend-only.md` | inline |
| 技术评审 | `technical-review/` | `review-template.md` | fork/Explore |
| 程序设计 | `program-design/` | `design-template.md` | inline |
| 任务拆分 | `task-breakdown/` | `task-breakdown-template.md` | fork/Plan |
| 单元测试 | `unit-testing/` | `test-case-template.md` | fork |
| 代码开发 | `code-development/` | `development-checklist.md` | inline |
| 自我验证 | `self-verification/` | `verification-template.md` | fork/Explore |

## 文档与状态管理

- 产出统一放在 `docs/` 下，按迭代+id 组织
- `docs/history.json` 记录迭代状态与各阶段 id
- 跨平台状态管理：`history-manager` skill
- 约定见 `docs-convention.md`
- 入口与顺序见 `CLAUDE.md`，总览见 `README.md`
