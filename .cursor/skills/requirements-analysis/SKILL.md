---
name: requirements-analysis
description: 梳理功能点与细节要求，产出结构化需求文档。在用户描述产品/项目需求、或明确要求做需求分析时使用；全栈工作流第一步。
---

# 需求分析

## 何时使用

- 用户描述了一个产品/项目想法，需要整理成可执行需求时。
- 全栈工作流中，作为第一步执行。

## 执行要点

1. **功能点梳理**：从用户描述中提取「功能模块 → 功能点」列表，不遗漏、不臆造。
2. **细节追问**：对模糊点（角色、边界、数据来源、异常情况）用 1～3 轮简短提问补全。
3. **输出格式**：使用 [templates/requirements-template.md](templates/requirements-template.md) 填写并产出需求文档。

## 产出

- 一份按模板填写的需求文档（功能点 + 细节要求），供「技术选型」与「程序设计」使用。

## 文档与状态

- 产出写入 **`docs/{current_iteration_id}/requirements-{requirements_id}.md`**。迭代 id 与阶段 id 见 **`docs/history.json`**；若该迭代已有 `phases.requirements_id` 且该文件存在，则**不重复生成**，除非用户要求重做。
- 写入后更新 `history.json`：该迭代的 `phases.requirements_id`、`state`、`updated_at`，及全局 `last_updated`。约定见 [docs-convention.md](../docs-convention.md)。

## 细节引导（可对用户提问）

- 用户角色与权限？（未登录/登录/多角色）
- 核心业务流程的步骤与异常分支？
- 数据来源与持久化要求？（仅前端 / 需要后端与数据库）
- 非功能：性能、安全、部署环境？
