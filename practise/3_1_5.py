from flask import Flask, render_template

app: Flask = Flask(__name__)


@app.route('/<float:r>/')
def index(r) -> render_template:
    return render_template('index.html',
                           r=r,
                           pi=3.14,
                           )


template = 'Площадь круга с радиусом {{ r }} равна {{ pi * r ** 2}}'
