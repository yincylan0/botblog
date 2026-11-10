"""BotBlog — 一个简单的 Python 博客网站（Flask）.

运行方式：
    pip install -r requirements.txt
    python app.py

生产环境（例如 Botkeep）：
    gunicorn app:app --bind 0.0.0.0:$PORT
"""

import os

import markdown
from flask import Flask, abort, render_template

from posts import POSTS

app = Flask(__name__)


def _render_md(text: str) -> str:
    """把 Markdown 转成 HTML（支持代码块、表格）。"""
    return markdown.markdown(
        text, extensions=["fenced_code", "tables", "toc"]
    )


@app.route("/")
def index():
    posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)
    return render_template("index.html", posts=posts)


@app.route("/post/<slug>")
def post(slug: str):
    found = next((p for p in POSTS if p["slug"] == slug), None)
    if found is None:
        abort(404)
    html = _render_md(found["content"])
    return render_template("post.html", post=found, content=html)


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def page_not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
