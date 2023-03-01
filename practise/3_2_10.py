{% macro get_solution() %}
    {% set temp = varargs | list %}
    {% for _ in varargs %}
        {% if (temp | sum) | string in kwargs.keys() %}
            {{ kwargs[(temp | sum) | string] }}
        {% endif %}
        {% set x = temp.pop() %}
    {% endfor %}
{% endmacro %}
