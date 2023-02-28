from flask import Flask, render_template
from random import choice


random_name: choice = choice(['Itgenio', 'Igor', 'Delictum'])
project_number = 100


app: Flask = Flask(__name__)


@app.route('/')
def index():
    return render_template('index2.html',
                           name='Itgenio',
                           title='Home page',
                           project_number=project_number)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)