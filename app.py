from flask import Flask, render_template, request, redirect, url_for
from random import choice
from project.forms import MessageForm
from config import Config

random_name: choice = choice(['Itgenio', 'Igor', 'Delictum'])
project_number = 100


app: Flask = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index2.html',
                           name='Itgenio',
                           title='Home page',
                           project_number=project_number)


@app.route('/message/', methods=['get', 'post'])
def message():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(name)
        print(email)
        print(message)
        print("\nData received. Now redirecting..")
        return redirect(url_for('message'))
    return render_template('message.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)