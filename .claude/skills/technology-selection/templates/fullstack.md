# 全栈技术选型模板

## 前端

| 项 | 选型 | 版本 | 说明 |
|----|------|------|------|
| 语言 | TypeScript / JavaScript | | 选一 |
| 框架 | React / Vue / Next.js / Nuxt / ... | | 与后端对接方式考虑 |
| UI 组件库 | Ant Design / MUI / Element Plus / shadcn/ui / 无 | | 与框架匹配 |
| 图标库 | Lucide / Heroicons / Ant Icons / FontAwesome / 无 | | |
| 状态管理 | Redux / Zustand / Pinia / ... | | 按需 |
| 请求库 | fetch / axios / ky / ... | | 与后端 API 约定一致 |
| 构建工具 | Vite / Webpack / Turbopack / ... | | |
| CSS 方案 | Tailwind / CSS Modules / styled-components / ... | | |
| 动画库 | Framer Motion / GSAP / Animate.css / 无 | | 按需 |

## 后端

| 项 | 选型 | 版本 | 说明 |
|----|------|------|------|
| 语言 | Java / TypeScript / Go / Python / ... | | 选一 |
| 框架 | Spring Boot / Express / Fastify / FastAPI / Gin / ... | | |
| API 风格 | REST / GraphQL | | 选一并约定规范 |
| 认证 | JWT / Session / OAuth2 / ... | | |
| API 文档 | Swagger/OpenAPI / 手写文档 / 无 | | 建议自动生成 |
| 日志框架 | SLF4J+Logback / Winston / Zap / logging / ... | | |
| 参数校验 | Hibernate Validator / Joi / Zod / Pydantic / ... | | |

## 数据与存储

| 项 | 选型 | 版本 | 说明 |
|----|------|------|------|
| 数据库 | PostgreSQL / MySQL / MongoDB / SQLite / ... | | 按需求选 |
| ORM/查询 | Prisma / TypeORM / MyBatis / SQLAlchemy / ... | | |
| 缓存 | Redis / 内存缓存 / 无 | | 按需 |

## 开发环境

| 项 | 要求 |
|----|------|
| Node 版本 | （如 >=20） |
| JDK 版本 | （如 21，若 Java） |
| Python 版本 | （如 >=3.11，若 Python） |
| 包管理器 | npm / yarn / pnpm / Maven / Gradle / pip / poetry |

## 测试

| 项 | 选型 | 说明 |
|----|------|------|
| 前端单测 | Jest / Vitest / ... | |
| 前端 E2E | Playwright / Cypress / 无 | 按需 |
| 后端单测 | JUnit / pytest / Jest / ... | |
| 后端集成测试 | Testcontainers / 内存数据库 / 无 | 按需 |

## 部署与运维

- 容器化：Docker / 无
- CI/CD：GitHub Actions / GitLab CI / 无
- 部署目标：本地 / 云服务 / Vercel / ...
- 监控/健康检查：Actuator / 自定义 /health / 无
