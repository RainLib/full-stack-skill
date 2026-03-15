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

## 执行要点

1. 参考需求文档中的非功能需求（性能、安全、部署）来约束选型。
2. 版本锁定：明确主要框架/库的版本号或版本范围。
3. 依赖管理：说明包管理器（npm/yarn/pnpm、Maven/Gradle、pip/poetry 等）。
4. 开发环境：Node 版本、JDK 版本、Python 版本等。

## 产出

- 一份技术选型清单，供「技术评审」与「程序设计」使用。

## 文档与状态

- 产出写入 `docs/{current_iteration_id}/technology-selection-{technology_selection_id}.md`。
- 开始前：调用 `history-manager` skill 的 `get-phase technology_selection` 和 `check-file` 确认是否已完成。
- 完成后：调用 `history-manager` skill 的 `set-phase technology_selection {technology_selection_id}` 记录并推进状态。
