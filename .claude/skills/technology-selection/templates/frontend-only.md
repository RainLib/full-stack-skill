# 仅前端技术选型模板

## 前端

| 项 | 选型 | 版本 | 说明 |
|----|------|------|------|
| 语言 | TypeScript / JavaScript | | 选一 |
| 框架 | React / Vue / Next.js / Nuxt / Svelte / ... | | 选一 |
| UI 组件库 | Ant Design / MUI / Element Plus / shadcn/ui / 无 | | 与框架匹配 |
| 图标库 | Lucide / Heroicons / Ant Icons / FontAwesome / 无 | | |
| 状态管理 | （按需） | | 本地状态 / 全局状态 |
| 数据来源 | Mock / 本地存储 / 静态 JSON / 已有 API | | 无后端时的数据方案 |
| 构建工具 | Vite / Webpack / ... | | |
| CSS 方案 | Tailwind / CSS Modules / ... | | |
| 动画库 | Framer Motion / GSAP / Animate.css / 无 | | 按需 |

## 开发环境

| 项 | 要求 |
|----|------|
| Node 版本 | （如 >=20） |
| 包管理器 | npm / yarn / pnpm |

## 测试

| 项 | 选型 | 说明 |
|----|------|------|
| 单元测试 | Jest / Vitest / ... | |
| E2E 测试 | Playwright / Cypress / 无 | 按需 |

## 部署

- 部署目标：Vercel / Netlify / GitHub Pages / 本地
- SSR/SSG：是 / 否

## 接口预留

- 若后续会接真实后端，预留 API 形状与协议（REST/GraphQL），约定 base URL 与 mock 切换方式。
