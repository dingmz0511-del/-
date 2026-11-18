# yt-dlp 视频下载工具

独立于 StoreMind AI 主项目，不会修改或依赖其后端代码。使用开源 [yt-dlp](https://github.com/yt-dlp/yt-dlp) 下载**有权下载的公开视频**。

## 方法一：直接在 GitHub Actions 使用（不需要安装软件）

1. 打开本仓库的 **Actions** 标签。
2. 选择 **Download video with yt-dlp** 工作流，点击 **Run workflow**。
3. 在 **video_url** 输入视频链接。留空则仅安装并检查 yt-dlp 版本。
4. 运行完成后，打开该次运行详情，在 **Artifacts** 下载 **downloaded-video**。
5. 运行生成的视频文件默认保留 3 天。

示例链接（需要平台允许访问）：

```text
https://xhslink.cn/o/8FTNyKpfSji
```

## 方法二：Windows PowerShell 本地运行

先安装 Python 3.11 或更新版本、FFmpeg，下载仓库源码并在仓库根目录执行：

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r tools/video-downloader/requirements.txt
python tools/video-downloader/download.py "https://xhslink.cn/o/8FTNyKpfSji"
```

视频默认保存到 `downloads/`。也可指定目录：

```powershell
python tools/video-downloader/download.py "https://example.com/video" --output my-videos
```

## 注意

- yt-dlp 支持网站列表中包括小红书，但不能保证每个分享链接都能下载；平台可能要求登录、校验或限制访问。
- GitHub Actions 在每次运行时临时安装 yt-dlp，并非 24 小时常驻服务。源码存放在仓库，视频以 Actions Artifacts 形式提供。
- 不要把浏览器 Cookie、账号密码或访问令牌提交到公开仓库，也不要下载无权获取的内容。
- **下载视频不等于自动提取字幕或生成摘要**；要进行内容总结，请另行提供视频或可用字幕。
