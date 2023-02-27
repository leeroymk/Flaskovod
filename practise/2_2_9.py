from flask import Flask

app: Flask = Flask(__name__)
# # Используемые арифметические операторы для этого задания
operations: tuple = ('+', ':', '**', '-', '*')


@app.route("/<string:link>/")
def query(link: str) -> str:
    for x in link:
        if x not in operations:
            pass
        else:
            if x != '*':
                res = list(map(int, link.split(x)))
                if x == '+':
                    return str(sum(res))
                elif x == ':':
                    return str(res[0] / res[1])
                elif x == '-':
                    return str(res[0] - res[1])
            else:
                res = link.split(x)
                if link.count(x) == 1:
                    return str(int(res[0]) * int(res[1]))
                else:
                    return str(int(res[0]) ** int(res[-1]))
