# src/web/app.py
from flask import Flask, render_template, request, redirect, url_for
from core.running import IdiomGame

app = Flask(__name__)
game = IdiomGame()


@app.route('/', methods=['GET', 'POST'])
def index():
    """首页：显示当前成语、处理用户输入"""
    message = ""
    success = None

    if request.method == 'POST':
        user_input = request.form.get('idiom', '').strip()
        if user_input:
            success, message = game.submit(user_input)
        else:
            success = False
            message = "请输入成语！"

    return render_template('index.html', game=game, message=message, success=success)


@app.route('/reset')
def reset():
    """重置游戏"""
    game.reset()
    return redirect(url_for('index'))
