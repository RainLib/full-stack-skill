# 代码开发自检清单

## 按任务自检

对每个已完成的任务（Task ID），逐条确认：

- [ ] 代码文件位置与设计文档的工程目录一致
- [ ] 该任务对应的所有测试用例已实现并通过
- [ ] 命名（变量、函数、类、文件）与项目约定一致
- [ ] 异常与边界按测试用例覆盖，无遗漏
- [ ] 无硬编码的密钥、密码或环境特定配置

## 按批次自检

每完成一个 Batch：

- [ ] 该批次所有任务的测试全部通过
- [ ] Lint 检查无新增错误
- [ ] 已提交或准备提交（附简要 commit message）

## 全局自检

所有任务完成后：

- [ ] 全量测试通过
- [ ] 目录结构与设计文档一致
- [ ] 无遗留 TODO/FIXME（或已标注为后续迭代）
- [ ] 开发过程中的偏差已记录到产出文档

## 运行命令参考

```bash
# 示例：根据实际项目调整
# 后端测试
cd backend && ./gradlew test        # Java/Gradle
cd backend && mvn test              # Java/Maven
cd backend && pytest                # Python
cd backend && npm test              # Node

# 前端测试
cd frontend && npm test             # Jest/Vitest
cd frontend && npm run lint         # ESLint

# 全量 lint
npm run lint                        # 或项目约定的 lint 命令
```
