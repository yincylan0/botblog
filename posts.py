"""博客文章：每篇一个 dict，content 用 Markdown 写。

新增文章：在这个列表里加一个 dict 即可，字段：
    slug    文章链接，如 "hello-world"，访问地址为 /post/hello-world
    title   标题
    date    日期（YYYY-MM-DD），首页按日期倒序排列
    summary 首页显示的简介
    content 正文（Markdown）
"""

POSTS = [
    {
        "slug": "hello-world",
        "title": "你好，世界",
        "date": "2026-11-10",
        "summary": "BotBlog 的第一篇文章：这个博客是怎么来的，能做什么。",
        "content": """# 你好，世界

欢迎来到 **BotBlog**，一个用 Python 和 Flask 写的简单博客。

这个博客没有数据库，文章就是代码里的 Markdown，改一行就能发布：

1. 在 `posts.py` 里加一篇文章
2. 提交到 GitHub
3. 部署到服务器

就这么简单。
""",
    },
    {
        "slug": "why-flask",
        "title": "为什么用 Flask 写博客",
        "date": "2026-11-10",
        "summary": "Flask 很小，但写博客刚好够用。",
        "content": """# 为什么用 Flask 写博客

Flask 的核心思想是**简单**：

- 一个文件就能跑起一个网站
- 路由、模板、静态文件都开箱即用
- 需要什么功能再加什么扩展，不需要的绝不强加

对一个小博客来说，Flask 的体量刚刚好——既不会像 Django 那样重，也不会像手写 WSGI 那样什么都得自己造。

> 简单不是简陋，是把复杂留给真正需要它的地方。
""",
    },
    {
        "slug": "deploy-to-botkeep",
        "title": "把博客部署到 Botkeep",
        "date": "2026-11-10",
        "summary": "从 GitHub 拉代码，用 Gunicorn 跑起来，博客就上线了。",
        "content": """# 把博客部署到 Botkeep

部署只需要三步：

```bash
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:$PORT
```

- `requirements.txt` 里是 Flask、Markdown 和 Gunicorn
- `app.py` 会读取 `PORT` 环境变量，平台给什么端口就监听什么端口
- 文章在 `posts.py` 里，更新文章只需要重新部署

部署完成后，就可以在浏览器里打开自己的博客了。
""",
    },
]
