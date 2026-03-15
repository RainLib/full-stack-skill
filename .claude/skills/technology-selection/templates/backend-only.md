# 仅后端技术选型模板

## 后端

| 项 | 选型 | 版本 | 说明 |
|----|------|------|------|
| 语言 | Java / TypeScript / Go / Python / ... | | 选一 |
| 框架 | Spring Boot / Express / Fastify / FastAPI / Gin / ... | | 选一 |
| API 风格 | REST / GraphQL | | 选一并约定请求/响应格式 |
| 认证 | JWT / Session / OAuth2 / ... | | |
| API 文档 | Swagger/OpenAPI / 手写文档 / 无 | | 建议自动生成 |
| 日志框架 | SLF4J+Logback / Winston / Zap / logging / ... | | |
| 参数校验 | Hibernate Validator / Joi / Zod / Pydantic / ... | | |

## 数据与存储

| 项 | 选型 | 版本 | 说明 |
|----|------|------|------|
| 数据库 | PostgreSQL / MySQL / MongoDB / SQLite / ... | | 按需求选 |
| ORM/查询 | MyBatis / TypeORM / SQLAlchemy / ... | | |
| 缓存 | Redis / 内存缓存 / 无 | | 按需 |

## 开发环境

| 项 | 要求 |
|----|------|
| JDK 版本 | （如 21，若 Java） |
| Node 版本 | （若 TypeScript/JS） |
| Python 版本 | （若 Python） |
| 包管理器 | Maven / Gradle / npm / pip / poetry |

## 测试

| 项 | 选型 | 说明 |
|----|------|------|
| 单元测试 | JUnit / pytest / Jest / ... | |
| 集成测试 | Testcontainers / 内存数据库 / 无 | 按需 |

## 部署

- 容器化：Docker / 无
- CI/CD：GitHub Actions / GitLab CI / 无
- 部署目标：本地 / 云服务 / ...
- 监控/健康检查：Actuator / 自定义 /health / 无

## 接口约定

- 明确 API 路径、方法、请求体/响应体形状，便于前端后续对接或 mock。
- 建议输出 OpenAPI/Swagger 规范文件。
