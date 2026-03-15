# 全栈技术选型清单

> 基于需求文档 `requirements-req-001.md`，开发范围：**全栈**

## 前端

| 项 | 选型 | 版本 | 说明 |
|----|------|------|------|
| 语言 | TypeScript | 5.x | 类型安全，团队已有经验 |
| 框架 | React | 18.x | 生态成熟，组件库丰富 |
| UI 组件库 | Ant Design | 5.x | 与需求中"Ant Design 风格"一致 |
| 图标库 | Ant Icons | 5.x | 与 Ant Design 配套 |
| 状态管理 | Zustand | 4.x | 轻量，适合中小型项目 |
| 请求库 | axios | 1.x | 拦截器支持好，便于统一错误处理 |
| 构建工具 | Vite | 5.x | 开发热更新快，构建速度优 |
| CSS 方案 | Ant Design 内置 + CSS Modules | - | 组件库样式为主，自定义部分用 CSS Modules |
| 动画库 | 无 | - | 当前需求无复杂动画 |
| 路由 | React Router | 6.x | |

## 后端

| 项 | 选型 | 版本 | 说明 |
|----|------|------|------|
| 语言 | Java | 21 | LTS 版本，用户指定 |
| 框架 | Spring Boot | 3.2.x | 生态完善，文档丰富 |
| API 风格 | REST | - | 需求简单 CRUD 为主，REST 足够 |
| 认证 | JWT（Spring Security） | - | 无状态，前后端分离友好 |
| API 文档 | SpringDoc OpenAPI | 2.x | 自动生成 Swagger UI |
| 日志框架 | SLF4J + Logback | - | Spring Boot 默认，JSON 格式输出 |
| 参数校验 | Hibernate Validator | - | Spring Boot 内置支持 |

## 数据与存储

| 项 | 选型 | 版本 | 说明 |
|----|------|------|------|
| 数据库 | PostgreSQL | 16.x | 用户指定，功能强大 |
| ORM | MyBatis-Plus | 3.5.x | 简化 CRUD，动态 SQL 灵活 |
| 缓存 | 无 | - | 初期数据量小，暂不需要 |

## 开发环境

| 项 | 要求 |
|----|------|
| JDK 版本 | 21 |
| Node 版本 | >=20 |
| 包管理器 | 前端 pnpm / 后端 Maven |

## 测试

| 项 | 选型 | 说明 |
|----|------|------|
| 前端单测 | Vitest | 与 Vite 集成好 |
| 前端 E2E | 无 | 初期不做 E2E |
| 后端单测 | JUnit 5 + Mockito | Spring Boot 默认 |
| 后端集成测试 | 无 | 初期不做 |

## 部署与运维

- 容器化：Docker（Dockerfile + docker-compose）
- CI/CD：暂无，后续可接 GitHub Actions
- 部署目标：单机 Docker Compose
- 监控/健康检查：Spring Boot Actuator `/actuator/health`
