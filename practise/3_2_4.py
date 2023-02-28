template = """
{% if operator == "+" %}
    {{ a + b }}
{% elif operator == "-" %}
    {{ a - b }}
{% elif operator == "*" %}
    {{ a * b }}
{% elif operator == "**" %}
    {{ a ** b }}
{% elif operator == ":" and b != 0 %}
    {{ a / b }}
{% else %}
    {{"Ошибка"}}
{% endif %}
"""

@app.route("/<float:a>/<string:operator>/<float:b>/")
def index(a, operator, b):
    return render_template(
        'index.html',
        a=a,
        b=b,
        operator=operator,
        template=template)
