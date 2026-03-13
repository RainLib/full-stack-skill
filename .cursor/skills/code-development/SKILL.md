---
name: code-development
description: 根据单元测试用例与程序设计实现代码，并通过测试验证。在单元测试设计之后使用，为全栈工作流最后一步。
---

# 代码开发

## 何时使用

- 全栈工作流中，在「单元测试」产出之后执行。
- 用户要求按测试或设计文档实现功能时。

## 输入

- 程序设计文档（结构、流程、目录）
- 单元测试用例文档（用例与预期）

## 执行要点

1. **顺序**：按设计文档的模块/目录创建或修改文件，先实现被依赖层（如数据层、工具），再业务与接口。
2. **测试驱动**：以测试用例为验收标准；实现一段则运行对应测试，通过后再继续。
3. **风格**：遵循项目既有风格与选型约定（如 Java 21、ESLint、命名规范）。

## 产出

- 可运行的代码与通过用例的测试；若某用例未通过，修正代码直至通过或更新用例文档并说明原因。

## 文档与状态

- 本阶段产出（代码与测试）在工程目录中实现；可在 **`docs/{current_iteration_id}/code-development-{code_development_id}.md`** 记录实现摘要或自检结果。阶段 id 见 **`docs/history.json`**；若该迭代已有 `phases.code_development_id` 且已完工，则**不重复生成**。
- 完成后更新 `history.json`：该迭代 `phases.code_development_id`、`state: "done"`、`updated_at` 及全局 `last_updated`。约定见 [docs-convention.md](../docs-convention.md)。

## 参考

- 工程目录与分层见「程序设计」产出。
- 断言与预期见 [templates/development-checklist.md](templates/development-checklist.md)（可选自检）。
