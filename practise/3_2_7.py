{% for key, value in numbers.items() %}
    {% if key.isdigit() %}
        {{ (key|int, value)|min }}
    {% endif %}
{% endfor %}