# Skill Frontmatter 规范

每个 skill 的 `SKILL.md` 必须以 YAML frontmatter 开头（`---` 包裹）。字段定义遵循 [Claude Code 官方规范](https://code.claude.com/docs/en/skills)。

## 字段列表

| 字段 | 必选 | 说明 |
|------|:----:|------|
| `name` | 否 | 技能标识，小写字母+数字+连字符，≤64 字符。省略时使用目录名。 |
| `description` | 推荐 | 技能用途与触发场景，供 Agent 判断何时加载。 |
| `argument-hint` | 否 | 自动补全时显示的参数提示，如 `[iteration-id]`、`[filename]`。 |
| `disable-model-invocation` | 否 | `true` 时 Agent 不会自动调用，仅用户通过 `/name` 手动触发。默认 `false`。 |
| `user-invocable` | 否 | `false` 时从 `/` 菜单隐藏，仅 Agent 可调用。默认 `true`。 |
| `allowed-tools` | 否 | 该 skill 激活时允许免确认使用的工具，逗号分隔。 |
| `context` | 否 | 设为 `fork` 时在隔离子 agent 中运行（无对话上下文）。 |
| `agent` | 否 | `context: fork` 时指定子 agent 类型：`Explore`、`Plan`、`general-purpose` 或自定义 agent。 |
| `model` | 否 | 指定该 skill 使用的模型。 |
| `hooks` | 否 | 该 skill 生命周期内的 hooks 配置。 |

## 调用控制矩阵

| 配置 | 用户可调 | Agent 可调 | 上下文加载 |
|------|:--------:|:----------:|-----------|
| 默认 | Yes | Yes | description 常驻，全文按需加载 |
| `disable-model-invocation: true` | Yes | No | description 不加载 |
| `user-invocable: false` | No | Yes | description 常驻，全文按需加载 |

## 本项目约定

- 编排入口 `dev-workflow`：`disable-model-invocation: true`（用户手动 `/dev-workflow`）。
- 各阶段 skill：`user-invocable: false`（隐藏菜单，由编排器调用）。
- 需要对话的阶段（requirements-analysis、technology-selection、program-design、code-development）不设 `context: fork`。
- 只读/生成类阶段（technical-review、task-breakdown、unit-testing、self-verification）设 `context: fork`。

## 示例

```yaml
---
name: dev-workflow
description: 全栈开发工作流编排器，按 8 阶段顺序执行。
argument-hint: [iteration-id]
disable-model-invocation: true
allowed-tools: Read, Write, Grep, Glob
---
```
