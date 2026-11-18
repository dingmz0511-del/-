# 店智 AI · StoreMind AI

面向中小型连锁餐饮企业的多门店 AI 运营管理 SaaS。

> 当前为 MVP 开发版本，不适合直接处理真实门店生产数据。

## 功能范围
- 多门店经营驾驶舱
- 库存管理和低库存预警
- 员工档案和任务管理
- 基于业务数据的 AI 店长问答
- PC / 手机响应式 Web 界面

## Windows PowerShell 启动
1. 下载并解压项目源码，进入包含 `backend` 文件夹的项目目录。
2. 安装 Python 3.10+，在 PowerShell 中执行：

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --app-dir backend --reload
```

3. 浏览器打开 http://127.0.0.1:8000 ，接口文档 http://127.0.0.1:8000/docs 。

若 PowerShell 阻止虚拟环境激活，先执行 `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`。

## 研发计划
1. 安全加固、租户隔离测试、数据库迁移和 CI。
2. POS 订单 CSV 导入、对账及真实数据模型。
3. 智能排班、库存预测、采购审批。
4. SOP 知识库、主动提醒和总部多门店分析。
5. SaaS 订阅、监控、备份与商业化部署。
6. 第二阶段接入摄像头和 IoT 设备。

## 项目源代码
完整项目包见当前对话提供的 `StoreMind_AI_GitHub_Ready_v0.1.1.zip`。请注意：仓库中尚未包含完整源码，上传前不要把它视为已部署产品。

## 安全
禁止提交 `.env`、数据库文件、GitHub Token、模型 API Key 或客户真实数据。

## 独立视频下载工具（yt-dlp）
已添加独立的 [yt-dlp 视频下载工具](tools/video-downloader/README.md)，可通过 [GitHub Actions](https://github.com/dingmz0511-del/-/actions/workflows/video-download.yml) 手动安装并下载支持的公开视频，无需运行 StoreMind AI 后端。
