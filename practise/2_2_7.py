from flask import Flask


app: Flask = Flask(__name__)


@app.route("/<int:var_name>/")
def query(var_name: int) -> str:
    return str(var_name + 1)
