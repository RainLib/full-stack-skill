# 技术评审文档

## 1. 评审范围

- **迭代**：iter-001
- **评审输入**：需求文档 `requirements-req-001.md` + 技术选型文档 `technology-selection-ts-001.md`
- **评审日期**：2025-01-15

## 2. 架构可行性

| 需求项 | 技术方案 | 可行性 | 备注 |
|--------|----------|:------:|------|
| 用户认证（JWT） | Spring Security + JWT | Yes | 成熟方案，无风险 |
| 订单 CRUD | Spring Boot + MyBatis-Plus + PostgreSQL | Yes | 标准模式 |
| 列表搜索与分页 | MyBatis-Plus 分页插件 + 条件构造 | Yes | 无需额外组件 |
| 订单状态流转 | 枚举 + 状态机校验 | Yes | 建议用有限状态机模式，避免 if/else |
| 数据导出 CSV | Apache POI / OpenCSV | Yes | 小数据量直接同步导出即可 |
| 前端侧边栏布局 | Ant Design ProLayout | Yes | 开箱即用 |
| 统计看板图表 | Ant Design Charts / ECharts | Risk | 需确认图表库选型，Ant Charts 偏重 |
| API 文档自动生成 | SpringDoc OpenAPI 2.x | Yes | 注解驱动 |

## 3. API 契约

### 3.1 接口列表

| 接口名 | 方法 | 路径 | 说明 |
|--------|------|------|------|
| 用户注册 | POST | /api/auth/register | |
| 用户登录 | POST | /api/auth/login | 返回 JWT |
| 获取当前用户 | GET | /api/users/me | |
| 订单列表 | GET | /api/orders | 分页 + 筛选 |
| 创建订单 | POST | /api/orders | |
| 订单详情 | GET | /api/orders/{id} | |
| 更新订单状态 | PATCH | /api/orders/{id}/status | |
| 导出订单 | GET | /api/orders/export | 返回 CSV 流 |
| 统计概览 | GET | /api/stats/overview | |

### 3.2 接口详情（核心接口）

**接口：创建订单**

- **路径**：`POST /api/orders`
- **请求体**：

```json
{
  "customerName": "string — 客户名称，必填",
  "customerContact": "string — 联系方式，选填",
  "items": [
    {
      "productName": "string — 商品名称",
      "quantity": "integer — 数量，>=1",
      "unitPrice": "decimal — 单价，>=0"
    }
  ],
  "remark": "string — 备注，选填"
}
```

- **响应体**（201）：

```json
{
  "id": "long — 订单 ID",
  "orderNo": "string — 订单编号（如 ORD-20250115-001）",
  "status": "string — PENDING",
  "totalAmount": "decimal — 自动计算",
  "createdAt": "string — ISO 时间"
}
```

- **错误码**：

| 状态码 | 含义 |
|--------|------|
| 400 | items 为空或参数校验失败 |
| 401 | 未认证 |
| 403 | 角色无创建权限（查看者） |

**接口：更新订单状态**

- **路径**：`PATCH /api/orders/{id}/status`
- **请求体**：

```json
{
  "action": "string — CONFIRM / COMPLETE / CANCEL"
}
```

- **响应体**（200）：

```json
{
  "id": "long",
  "status": "string — 新状态",
  "updatedAt": "string"
}
```

- **错误码**：

| 状态码 | 含义 |
|--------|------|
| 400 | 非法状态转换（如已完成→确认） |
| 404 | 订单不存在 |

## 4. 数据模型

### 4.1 核心实体

| 实体 | 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|------|
| user | id | bigint | PK, auto | |
| user | email | varchar(255) | UNIQUE, NOT NULL | |
| user | password_hash | varchar(255) | NOT NULL | bcrypt |
| user | name | varchar(100) | NOT NULL | |
| user | role | varchar(20) | NOT NULL | ADMIN/OPERATOR/VIEWER |
| order | id | bigint | PK, auto | |
| order | order_no | varchar(30) | UNIQUE, NOT NULL | 业务编号 |
| order | customer_name | varchar(200) | NOT NULL | |
| order | status | varchar(20) | NOT NULL | PENDING/PROCESSING/COMPLETED/CANCELLED |
| order | total_amount | decimal(12,2) | NOT NULL | |
| order | created_by | bigint | FK → user.id | |
| order_item | id | bigint | PK, auto | |
| order_item | order_id | bigint | FK → order.id | |
| order_item | product_name | varchar(200) | NOT NULL | |
| order_item | quantity | integer | NOT NULL, >=1 | |
| order_item | unit_price | decimal(10,2) | NOT NULL, >=0 | |
| order_log | id | bigint | PK, auto | |
| order_log | order_id | bigint | FK → order.id | |
| order_log | action | varchar(50) | NOT NULL | CREATE/CONFIRM/COMPLETE/CANCEL |
| order_log | operator_id | bigint | FK → user.id | |
| order_log | created_at | timestamp | NOT NULL, DEFAULT NOW() | |

### 4.2 实体关系

- User 1 --- N Order（created_by）
- Order 1 --- N OrderItem
- Order 1 --- N OrderLog
- User 1 --- N OrderLog（operator_id）

## 5. 风险清单

| 编号 | 风险描述 | 影响 | 概率 | 建议对策 |
|------|----------|------|------|----------|
| R1 | 订单状态流转逻辑散落在多处 | 中 | 中 | 抽取状态机类，集中管理合法转换 |
| R2 | CSV 导出大数据量时内存溢出 | 中 | 低 | 使用流式写入，设单次导出上限 |
| R3 | JWT 过期后前端无自动刷新 | 中 | 高 | 实现 refresh token 或前端拦截 401 重新登录 |
| R4 | 图表库选型未确定 | 低 | 中 | 建议使用 @ant-design/charts 或 ECharts，程序设计阶段确认 |

## 6. 评审结论

- **结论**：有条件通过
- **必须修正项**：
  1. R3：JWT 刷新机制需在程序设计阶段明确方案
  2. R4：图表库需在技术选型中补充确认
- **建议优化项**：
  - R1：建议引入简单状态机模式
  - 数据导出建议设置行数上限（如 10000 行）
