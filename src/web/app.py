# src/web/app.py
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    """首页"""
    return "Hello, Flask!"


@app.route('/reset')
def reset():
    """重置游戏"""
    return redirect(url_for('index'))
