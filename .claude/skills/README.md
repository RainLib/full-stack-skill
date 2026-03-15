# 全栈 Skills 工作流

本目录定义「需求分析 → 技术选型 → 技术评审 → 程序设计 → 任务拆分 → 单元测试 → 代码开发 → 自我验证」的标准化 8 阶段工作流。

## 工作流

```
/dev-workflow → 需求分析 → 技术选型 → 技术评审 → 程序设计
              → 任务拆分 → 单元测试 → 代码开发 → 自我验证 → done
```

| 顺序 | 阶段 | 目录 | 产出 | 调用方式 |
|:----:|------|------|------|----------|
| - | 编排入口 | `dev-workflow/` | 读写 history，调度各阶段 | 用户 `/dev-workflow` |
| 1 | 需求分析 | `requirements-analysis/` | 需求文档 | inline |
| 2 | 技术选型 | `technology-selection/` | 选型清单 | inline |
| 3 | 技术评审 | `technical-review/` | 评审文档（API 契约、数据模型、风险） | fork/Explore |
| 4 | 程序设计 | `program-design/` | 设计文档（分层、流程、目录） | inline |
| 5 | 任务拆分 | `task-breakdown/` | 任务列表（批次、依赖、优先级） | fork/Plan |
| 6 | 单元测试 | `unit-testing/` | 测试用例文档 | fork |
| 7 | 代码开发 | `code-development/` | 代码 + 实现摘要 | inline |
| 8 | 自我验证 | `self-verification/` | 验证报告 | fork/Explore |

## 目录结构

```
skills/
├── README.md                    # 本文件：工作流总览
├── CLAUDE.md                    # Agent 入口：阶段顺序与调用方式
├── SKILL_META.md                # Frontmatter 字段规范
├── docs-convention.md           # 文档与状态管理约定
├── task.md                      # 工作流原始定义
├── history-manager/             # 状态管理 skill（被其他 skill 调用）
│   ├── SKILL.md
│   └── scripts/
│       └── history_manager.py  # 跨平台 Python 3 工具
├── dev-workflow/                # 编排入口（/dev-workflow）
│   └── SKILL.md
├── requirements-analysis/       # 需求分析
│   ├── SKILL.md
│   └── templates/
├── technology-selection/        # 技术选型
│   ├── SKILL.md
│   └── templates/
├── technical-review/            # 技术评审
│   ├── SKILL.md
│   └── templates/
├── program-design/              # 程序设计
│   ├── SKILL.md
│   └── templates/
├── task-breakdown/              # 任务拆分
│   ├── SKILL.md
│   └── templates/
├── unit-testing/                # 单元测试
│   ├── SKILL.md
│   └── templates/
├── code-development/            # 代码开发
│   ├── SKILL.md
│   └── templates/
└── self-verification/           # 自我验证
    ├── SKILL.md
    └── templates/
```

## 文档与状态管理

- 所有阶段产出写入项目 `docs/` 目录，按迭代 id 组织：`docs/{iteration_id}/`。
- `docs/history.json` 记录当前迭代、各阶段 id、状态与时间，避免重复生成。
- 跨平台操作通过 `history-manager` skill（内置 Python 3 脚本，macOS + Windows）。
- **工程管理**使用项目根目录的 `Makefile`，运行 `make help` 查看所有可用命令。
- 约定见 [docs-convention.md](docs-convention.md)；文档目录说明见 [docs/README.md](../../docs/README.md)。
- Frontmatter 规范见 [SKILL_META.md](SKILL_META.md)。
