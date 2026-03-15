---
name: self-verification
description: 代码开发完成后运行全量测试、检查集成、代码质量自检，产出验证报告。在代码开发之后使用，为全栈工作流最后一步。
user-invocable: false
allowed-tools: Read, Grep, Glob, Bash(*)
context: fork
agent: Explore
---

# 自我验证

## 何时使用

- 全栈工作流第 8 阶段：代码开发完成后。
- 用户要求做集成验证或质量自检时。

## 输入

读取当前迭代目录下的全部阶段文档，以及工程中的代码和测试文件。

## 执行要点

1. **单元测试**：运行全量单元测试，记录通过/失败/跳过数量。
2. **集成验证**：若有 API 或前后端联调点，运行集成/冒烟测试或手动检查。
3. **代码质量**：
   - Lint 检查（运行项目配置的 linter）
   - 命名与目录与设计文档一致性
   - 无遗留 TODO/FIXME（或已标注为后续迭代）
4. **覆盖率**：若项目配置了覆盖率工具，运行并记录核心模块覆盖率。
5. **对照验收**：逐条核对任务拆分中的验收标准是否满足。

## 产出

- 使用 [templates/verification-template.md](templates/verification-template.md) 产出验证报告。

## 验证结论

- **通过**：所有测试通过、验收标准满足 → 迭代状态设为 `done`。
- **未通过**：列出失败项 → 回退到 code-development 修复，修复后重新验证。

## 文档与状态

- 产出写入 `docs/{current_iteration_id}/self-verification-{self_verification_id}.md`。
- 开始前：调用 `history-manager` skill 的 `get-phase self_verification` 和 `check-file` 确认是否已完成。
- 通过时：调用 `history-manager` skill 的 `set-phase self_verification {self_verification_id}` 记录并推进状态至 `done`。
- 未通过时：不调用 `set-phase`，保持 `self_verification` 状态，待修复后重新运行。
