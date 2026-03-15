---
name: unit-testing
description: 根据程序设计与任务拆分产出单元测试用例与预期结果，为代码开发提供验收标准。全栈工作流第 6 阶段。
user-invocable: false
allowed-tools: Read, Write, Grep
context: fork
---

# 单元测试设计

## 何时使用

- 全栈工作流第 6 阶段：任务拆分完成后、代码开发之前。
- 用户要求先写测试或设计测试用例时。

## 输入

读取当前迭代目录下的：
- 程序设计文档（`program-design-{id}.md`）—— 模块、接口、数据模型
- 任务拆分文档（`task-breakdown-{id}.md`）—— 按任务单元组织用例

## 执行要点

1. **按任务组织**：以任务拆分中的任务 ID 为单位组织测试用例。
2. **粒度**：以「可测单元」为单位（函数、类方法、API 端点、前端逻辑块）。
3. **覆盖**：正常路径 + 边界（空值、上限、类型错误） + 异常（网络失败、权限不足）。
4. **预期**：每个用例写明预期结果或断言要点（返回值、状态码、副作用、UI 状态）。
5. **Mock 策略**：标注哪些依赖需要 mock（数据库、外部 API、文件系统）。
6. **覆盖率目标**：核心业务模块建议 ≥80%，工具/配置类可放宽。

## 产出

- 使用 [templates/test-case-template.md](templates/test-case-template.md) 产出测试用例文档，供「代码开发」按用例实现并验证。

## 文档与状态

- 产出写入 `docs/{current_iteration_id}/unit-testing-{unit_testing_id}.md`。
- 开始前：调用 `history-manager` skill 的 `get-phase unit_testing` 和 `check-file` 确认是否已完成。
- 完成后：调用 `history-manager` skill 的 `set-phase unit_testing {unit_testing_id}` 记录并推进状态。
