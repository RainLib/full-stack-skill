---
name: technology-selection
description: 根据全栈/仅前端/仅后端选择技术栈并产出选型清单。全栈工作流第 2 阶段，需先询问用户开发范围。
user-invocable: false
allowed-tools: Read, Write
---

# 技术选型

## 何时使用

- 全栈工作流第 2 阶段：需求分析完成后、技术评审之前。
- 用户明确说要做技术选型或确定技术栈时。

## 与用户交流（必须）

本阶段在**主对话中执行**，必须与用户交流，不得自行假定或跳过对话直接产出文档。

1. **先问再写**：先向用户确认开发范围（见下方三选一），得到用户**明确答复**后，再根据选择进入对应模板并生成选型清单。
2. **可选追问**：若需求文档中有多种技术路线（如前端框架偏好、后端语言），可列出 2～3 个选项请用户选择后再写入文档。

## 第一步：确认开发范围

**必须先问用户**（三选一）：

- **全栈开发**：前端 + 后端 + 数据存储
- **仅前端开发**：界面与前端逻辑，数据可 mock 或本地
- **仅后端开发**：API、业务逻辑、数据库，不含界面

根据用户选择，进入对应模板与引导。

## 选型引导

- **全栈**：见 [templates/fullstack.md](templates/fullstack.md)
- **仅前端**：见 [templates/frontend-only.md](templates/frontend-only.md)
- **仅后端**：见 [templates/backend-only.md](templates/backend-only.md)

## 第二步：逐项确认选型（需与用户对话）

确认开发范围后，**按模板中的各项逐步与用户确认**，而非一次性假定全部选型：

### 涉及前端时，额外需确认：

- **UI 组件库**：Ant Design / MUI / Element Plus / shadcn/ui / 手写 / 无偏好？
- **图标库**：Lucide / Heroicons / Ant Icons / FontAwesome / 无偏好？
- **CSS 方案**：Tailwind / CSS Modules / styled-components / 无偏好？
- **动画需求**：Framer Motion / GSAP / 不需要动画？

### 涉及后端时，额外需确认：

- **API 文档生成**：Swagger/OpenAPI 自动生成 / 手写 / 暂不需要？
- **日志框架**：SLF4J+Logback / Winston / Zap / 无偏好？
- **参数校验**：Hibernate Validator / Joi / Zod / Pydantic / 无偏好？
- **测试框架**：JUnit / pytest / Jest / 无偏好？

## 执行要点

1. 参考需求文档中的非功能需求（性能、安全、部署）和 UI/UX 偏好来约束选型。
2. 版本锁定：明确主要框架/库的版本号或版本范围。
3. 依赖管理：说明包管理器（npm/yarn/pnpm、Maven/Gradle、pip/poetry 等）。
4. 开发环境：Node 版本、JDK 版本、Python 版本等。
5. 测试工具：单测框架、E2E 框架（若需要）。

## 辅助资料

- 完整示例输出：[examples/sample-output.md](examples/sample-output.md) — 展示一份合格选型清单的完整结构
- 选型参考：[reference.md](reference.md) — 常见全栈组合、框架/组件库/数据库对比、选型决策原则

## 产出

- 一份技术选型清单，供「技术评审」与「程序设计」使用。

## 文档与状态

- 产出写入 `docs/{current_iteration_id}/technology-selection-{technology_selection_id}.md`。
- 开始前：调用 `history-manager` skill 的 `get-phase technology_selection` 和 `check-file` 确认是否已完成。
- 完成后：调用 `history-manager` skill 的 `set-phase technology_selection {technology_selection_id}` 记录并推进状态。
