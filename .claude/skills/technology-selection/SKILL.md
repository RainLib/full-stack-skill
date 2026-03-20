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

### 交互原则

- **所有决策点都应以结构化选项呈现**，让用户选择而非自由输入。
- 一次不要问超过 3 个问题，避免信息过载。
- 每轮问完等用户回复后再进入下一轮，不得一次性抛出全部问题。
- 允许用户在选项之外补充（选"其他"或"无偏好"后可追加说明）。

## 结构化提问引导

根据需求文档中已确定的开发范围，**按轮次向用户呈现选项**。

### 第 1 轮：开发范围确认

> 若需求文档已明确开发范围，可跳过本轮。

**Q1 — 开发范围？**
- A. 全栈开发（前端 + 后端 + 数据存储）
- B. 仅前端（界面与前端逻辑，数据 mock 或本地）
- C. 仅后端（API + 数据库，不含界面）

根据用户选择，进入对应模板：
- **A**：见 [templates/fullstack.md](templates/fullstack.md)
- **B**：见 [templates/frontend-only.md](templates/frontend-only.md)
- **C**：见 [templates/backend-only.md](templates/backend-only.md)

### 第 2 轮：前端选型（涉及前端时）

**Q2 — 前端框架？**
- A. React
- B. Vue
- C. Next.js
- D. Nuxt
- E. Svelte
- F. 其他（请说明）

**Q3 — UI 组件库？**
- A. Ant Design
- B. MUI (Material UI)
- C. Element Plus
- D. shadcn/ui
- E. 不使用组件库（手写）
- F. 无偏好，按框架推荐

**Q4 — CSS 方案？**
- A. Tailwind CSS
- B. CSS Modules
- C. styled-components / Emotion
- D. 组件库自带样式即可
- E. 无偏好

### 第 3 轮：后端选型（涉及后端时）

**Q5 — 后端语言？**
- A. Java
- B. TypeScript (Node.js)
- C. Go
- D. Python
- E. 其他（请说明）

**Q6 — 后端框架？**（根据 Q5 的语言给出对应选项）
- Java: A. Spring Boot / B. Quarkus
- TypeScript: A. Express / B. Fastify / C. NestJS
- Go: A. Gin / B. Echo
- Python: A. FastAPI / B. Django

**Q7 — 数据库？**
- A. PostgreSQL
- B. MySQL
- C. MongoDB
- D. SQLite
- E. 无偏好，你来推荐

### 第 4 轮：补充选型

**Q8 — 测试框架？**（根据已选语言给出对应选项）
- 前端: A. Vitest / B. Jest / C. 后续再定
- 后端 Java: A. JUnit 5 / B. 后续再定
- 后端 TS: A. Jest / B. Vitest / C. 后续再定
- 后端 Python: A. pytest / B. 后续再定

**Q9 — 包管理器？**（根据已选语言给出对应选项）
- 前端: A. pnpm / B. yarn / C. npm
- Java: A. Maven / B. Gradle
- Python: A. pip / B. poetry

**Q10 — 还有其他技术偏好想补充吗？**（开放式，可回答"没有了"）

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
