---
name: technology-selection
description: 根据全栈/仅前端/仅后端选择技术栈并产出选型清单。在需求分析之后、程序设计之前使用；需先询问用户开发范围。
---

# 技术选型

## 何时使用

- 全栈工作流中，在「需求分析」产出之后、「程序设计」之前执行。
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

## 产出

- 一份技术选型清单（语言、框架、库、数据库/存储等），供「程序设计」使用。

## 文档与状态

- 产出写入 **`docs/{current_iteration_id}/technology-selection-{technology_selection_id}.md`**。阶段 id 见 **`docs/history.json`**；若该迭代已有 `phases.technology_selection_id` 且该文件存在，则**不重复生成**。
- 写入后更新 `history.json` 中该迭代的 `phases.technology_selection_id`、`state`、`updated_at` 及全局 `last_updated`。约定见 [docs-convention.md](../docs-convention.md)。
