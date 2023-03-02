from flask import Flask, request, render_template, abort

app = Flask(__name__)

news: dict = {}
@app.route("/", methods=["POST", "GET"])
def render_send(news):
    req_title = ''
    req_news = ''
    if request.method == "POST":
        req_title = request.form.get('title')
        req_content = request.form.get('content')
        news[req_title] = req_content
        if not req_title or not req_content:
            abort(404)
    return render_template('index.html',
                           news=news)
