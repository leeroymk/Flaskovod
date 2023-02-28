from flask import Flask, render_template

app: Flask = Flask(__name__)


@app.route('/<float:number>/')
def index(number) -> render_template:
    return render_template('index.html',
                           text=f'Ваше число {number}, умноженное на 2: {number * 2}')
