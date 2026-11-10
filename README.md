# BotBlog

一个简单的 Python 博客网站，用 Flask 写成。没有数据库，文章就是 `posts.py` 里的 Markdown。

## 本地运行

```bash
pip install -r requirements.txt
python app.py
```

打开 http://127.0.0.1:5000 即可访问。

## 生产部署

```bash
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:$PORT
```

应用会读取 `PORT` 环境变量（平台提供），监听 `0.0.0.0`。

## 写文章

在 `posts.py` 的 `POSTS` 列表里加一个 dict：

```python
{
    "slug": "my-post",          # 访问地址：/post/my-post
    "title": "文章标题",
    "date": "2026-11-10",
    "summary": "首页显示的简介",
    "content": "正文（Markdown）",
}
```

## 目录结构

```
app.py            Flask 应用：路由、Markdown 渲染
posts.py          全部文章
requirements.txt  Flask、Markdown、Gunicorn
templates/        base / index / post / about / 404
static/style.css  样式
```
