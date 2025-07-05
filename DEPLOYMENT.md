# 项目部署指南

## 项目状态检查清单

### ✅ 已完成
- [x] 项目结构设置
- [x] FastAPI后端应用
- [x] 前端HTML界面
- [x] Docker配置
- [x] GitHub Actions CI/CD工作流
- [x] MLflow模型管理
- [x] DVC数据版本控制
- [x] 测试用例（单元测试、集成测试、端到端测试）

### 🔄 需要完成的步骤

## 1. 分支管理设置

```bash
# 创建开发分支
git checkout -b dev
git push -u origin dev

# 创建staging分支
git checkout -b staging
git push -u origin staging

# 返回main分支
git checkout main
```

## 2. 配置GitHub Secrets

在GitHub仓库设置中添加以下secrets：

- `DOCKERHUB_USER`: 你的DockerHub用户名
- `DOCKERHUB_TOKEN`: 你的DockerHub访问令牌

## 3. 测试本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 启动应用
uvicorn src.app:app --host 0.0.0.0 --port 8000

# 运行测试
pytest tests/

# 访问前端界面
# http://localhost:8000/ui
```

## 4. 部署到云平台

### 选项1: Koyeb (推荐)

1. 访问 [koyeb.com](https://koyeb.com)
2. 注册并登录
3. 点击 "Create App"
4. 选择 "Docker" 部署方式
5. 输入Docker镜像: `zihaobao/dev_project:latest`
6. 设置端口: `8000`
7. 点击 "Deploy"

### 选项2: Railway

1. 访问 [railway.app](https://railway.app)
2. 连接GitHub仓库
3. 选择项目
4. 配置环境变量（如果需要）
5. 自动部署

### 选项3: AWS/GCP/Azure

按照各平台的Docker容器部署指南进行配置。

## 5. 更新端到端测试

部署完成后，更新 `tests/test_e2e.py` 中的URL：

```python
BASE_URL = "https://your-deployed-app-url.com"
```

## 6. 验证部署

1. 访问部署的URL
2. 测试 `/` 端点
3. 测试 `/ui` 前端界面
4. 测试 `/predict` 预测功能
5. 运行端到端测试

## 7. 最终检查清单

- [ ] 所有分支已创建 (dev, staging, main)
- [ ] GitHub Secrets已配置
- [ ] CI/CD工作流正常运行
- [ ] Docker镜像成功推送到DockerHub
- [ ] 应用成功部署到云平台
- [ ] 前端界面可正常访问
- [ ] 预测功能正常工作
- [ ] 所有测试通过
- [ ] 提供可公开访问的URL

## 故障排除

### 常见问题

1. **Docker构建失败**
   - 检查Dockerfile语法
   - 确保所有依赖都在requirements.txt中

2. **模型加载失败**
   - 检查MLflow模型路径
   - 确保模型文件存在

3. **部署失败**
   - 检查云平台配置
   - 验证端口设置
   - 检查环境变量

4. **测试失败**
   - 更新测试中的URL
   - 检查网络连接
   - 验证API响应格式

## 项目URL

部署完成后，请在此处添加你的应用URL：

**应用URL**: `https://your-app-url.com`

**前端界面**: `https://your-app-url.com/ui`

**API文档**: `https://your-app-url.com/docs` 