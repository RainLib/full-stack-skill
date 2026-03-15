# 技术选型参考指南

## 常见全栈组合

### Java 全栈

| 前端 | 后端 | 数据库 | 适用场景 |
|------|------|--------|----------|
| React + Ant Design | Spring Boot | PostgreSQL / MySQL | 企业后台、管理系统 |
| Vue + Element Plus | Spring Boot | MySQL | 中后台系统 |
| Next.js | Spring Boot | PostgreSQL | 需要 SEO 的业务系统 |

### TypeScript 全栈

| 前端 | 后端 | 数据库 | 适用场景 |
|------|------|--------|----------|
| React + MUI | Express / Fastify | PostgreSQL + Prisma | 快速原型、中小型应用 |
| Next.js | Next.js API Routes | PostgreSQL + Prisma | 全栈一体、部署简单 |
| Vue + shadcn/ui | Fastify | MongoDB + Mongoose | 灵活数据结构 |

### Python 全栈

| 前端 | 后端 | 数据库 | 适用场景 |
|------|------|--------|----------|
| React | FastAPI | PostgreSQL + SQLAlchemy | AI/ML 相关、数据密集 |
| Vue | Django | PostgreSQL | 内容管理、快速开发 |

## 前端框架选型对比

| 框架 | 优势 | 劣势 | 适用 |
|------|------|------|------|
| React | 生态最大、社区活跃、招聘容易 | 选择多易迷茫 | 大多数项目 |
| Vue | 上手快、文档好、中文友好 | 大型项目生态不如 React | 中小型项目 |
| Next.js | SSR/SSG、文件路由、全栈能力 | 框架约束多 | 需要 SEO / 全栈 |
| Svelte | 性能好、包体积小 | 生态小、组件库少 | 性能敏感的小项目 |

## UI 组件库选型对比

| 组件库 | 框架 | 风格 | 特点 |
|--------|------|------|------|
| Ant Design | React | 商务/企业 | 功能全面，中后台首选 |
| MUI | React | Material | Google 风格，定制灵活 |
| shadcn/ui | React | 现代简约 | 复制粘贴式，完全可控 |
| Element Plus | Vue | 商务/简洁 | Vue 生态首选 |
| Vuetify | Vue | Material | Material 风格 Vue 版 |

## 后端框架选型对比

| 框架 | 语言 | 优势 | 适用 |
|------|------|------|------|
| Spring Boot | Java | 企业级、生态完善、稳定 | 企业应用、大型系统 |
| Express | Node.js | 轻量灵活、上手快 | 简单 API、快速原型 |
| Fastify | Node.js | 高性能、schema 校验 | 性能敏感的 API |
| FastAPI | Python | 类型提示、自动文档、异步 | AI/ML 后端、数据服务 |
| Gin | Go | 高性能、编译型 | 高并发微服务 |

## 数据库选型对比

| 数据库 | 类型 | 优势 | 适用 |
|--------|------|------|------|
| PostgreSQL | 关系型 | 功能最强、扩展性好 | 通用首选 |
| MySQL | 关系型 | 成熟稳定、运维资料多 | 中小型应用 |
| MongoDB | 文档型 | 灵活 schema、水平扩展 | 文档/日志类数据 |
| SQLite | 嵌入式 | 零配置、单文件 | 本地应用、原型 |

## ORM/查询库对比

| 工具 | 语言 | 特点 |
|------|------|------|
| MyBatis-Plus | Java | SQL 灵活，CRUD 自动化 |
| JPA/Hibernate | Java | 标准 ORM，适合简单模型 |
| Prisma | TypeScript | 类型安全，迁移方便 |
| TypeORM | TypeScript | 装饰器风格，功能全 |
| SQLAlchemy | Python | 功能最强的 Python ORM |
| Drizzle | TypeScript | 轻量、类型安全、SQL-like |

## 选型决策原则

1. **团队熟悉度优先**：选团队最熟悉的技术，降低学习成本
2. **生态成熟度**：优先选择社区活跃、文档完善的方案
3. **需求匹配**：技术能力要能覆盖非功能需求（性能、安全等）
4. **避免过度工程**：初期不用最复杂的方案，可以逐步演进
5. **版本策略**：优先 LTS 版本，锁定主要依赖版本范围
