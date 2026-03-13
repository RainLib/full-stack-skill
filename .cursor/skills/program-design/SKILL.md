---
name: program-design
description: 根据需求与技术选型设计程序结构、流程与工程目录。在技术选型之后、单元测试之前使用。
---

# 程序设计

## 何时使用

- 全栈工作流中，在「技术选型」产出之后、「单元测试」之前执行。
- 用户要求做架构设计、模块划分或工程结构时。

## 输入

- 需求文档（功能点与细节）
- 技术选型清单（全栈/前端/后端及技术栈）

## 执行要点

1. **结构**：按选型划分模块/层（如前端页面与组件、后端控制器/服务/仓储、数据模型）。
2. **流程**：关键业务流程的调用顺序、接口边界、数据流。
3. **工程目录**：给出推荐目录结构，与选型一致（见模板）。

## 产出

- 使用 [templates/design-template.md](templates/design-template.md) 产出一份设计文档（结构 + 流程 + 目录），供「单元测试」与「代码开发」使用。

## 文档与状态

- 产出写入 **`docs/{current_iteration_id}/program-design-{program_design_id}.md`**。阶段 id 见 **`docs/history.json`**；若该迭代已有 `phases.program_design_id` 且该文件存在，则**不重复生成**。
- 写入后更新 `history.json` 中该迭代的 `phases.program_design_id`、`state`、`updated_at` 及全局 `last_updated`。约定见 [docs-convention.md](../docs-convention.md)。
