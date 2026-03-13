---
name: unit-testing
description: 根据程序设计产出单元测试用例与预期结果，为代码开发提供验收标准。在程序设计之后、代码开发之前使用。
---

# 单元测试设计

## 何时使用

- 全栈工作流中，在「程序设计」产出之后、「代码开发」之前执行。
- 用户要求先写测试或设计测试用例时。

## 输入

- 程序设计文档（模块、接口、流程、目录）

## 执行要点

1. **粒度**：以「可测单元」为单位（函数、类、API 端点、前端逻辑块）。
2. **用例**：正常路径 + 边界与异常（空输入、非法参数、失败分支）。
3. **预期**：每个用例写明预期结果或断言要点（返回值、状态码、副作用）。

## 产出

- 使用 [templates/test-case-template.md](templates/test-case-template.md) 产出测试用例文档，供「代码开发」按用例实现并验证。

## 文档与状态

- 产出写入 **`docs/{current_iteration_id}/unit-testing-{unit_testing_id}.md`**。阶段 id 见 **`docs/history.json`**；若该迭代已有 `phases.unit_testing_id` 且该文件存在，则**不重复生成**。
- 写入后更新 `history.json` 中该迭代的 `phases.unit_testing_id`、`state`、`updated_at` 及全局 `last_updated`。约定见 [docs-convention.md](../docs-convention.md)。
