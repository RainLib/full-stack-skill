# 全栈 Skills 工作流

本目录定义「需求分析 → 技术选型 → 程序设计 → 单元测试 → 代码开发」的标准化工作流，供 Agent 按顺序执行。

## 工作流顺序

```
需求分析 → 技术选型 → 程序设计 → 单元测试 → 代码开发
```

| 阶段       | 目录                    | 产出概要 |
|------------|-------------------------|----------|
| 需求分析   | `requirements-analysis/` | 功能点列表、细节要求（见模板） |
| 技术选型   | `technology-selection/`  | 全栈/仅前端/仅后端 + 技术栈清单 |
| 程序设计   | `program-design/`       | 程序结构、流程、工程目录 |
| 单元测试   | `unit-testing/`         | 测试用例与预期结果 |
| 代码开发   | `code-development/`     | 按测试实现的代码 |

## 目录结构

```
skills/
├── README.md                 # 本文件：工作流总览
├── CLAUDE.md                 # Agent 入口：何时用哪个 skill、顺序
├── task.md                   # 工作流定义与要求
├── requirements-analysis/    # 需求分析
│   ├── SKILL.md
│   └── templates/
├── technology-selection/     # 技术选型（全栈/前端/后端分支）
│   ├── SKILL.md
│   └── templates/
├── program-design/           # 程序设计
│   ├── SKILL.md
│   └── templates/
├── unit-testing/             # 单元测试
│   ├── SKILL.md
│   └── templates/
├── code-development/         # 代码开发
│   ├── SKILL.md
│   └── templates/
├── pku-requirements-analysis-skill/   # 需求分析别名，指向 requirements-analysis
└── pku-technology-selection-skill/    # 技术选型别名，指向 technology-selection
```

## 使用方式

- 从「需求分析」开始：用户描述需求后，先执行 `requirements-analysis`，再按顺序进入后续 skill。
- 技术选型时：先询问「全栈 / 仅前端 / 仅后端」，再进入对应引导与模板。
- 各 skill 的 SKILL.md 保持轻量；细节与模板放在各自 `templates/` 或引用文件中。

## 文档与状态管理

- 所有阶段产出写入项目 **`docs/`** 目录，按 **迭代 id** 组织：`docs/{iteration_id}/`，如 `docs/iter-001/`。
- **`docs/history.json`** 记录当前迭代、各阶段 id（避免重复生成）、创建时间与更新时间。
- 状态与书写约定见 [docs-convention.md](docs-convention.md)；文档目录说明见项目根下 [docs/README.md](../../docs/README.md)。
