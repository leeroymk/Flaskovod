{% macro post_email(email, message, title=1) %}
    {% if '@' not in email %}
        E-mail '{{email}}' некорректный
    {% else %}
        Сообщение '{{ message }}' для адресата '{{ email }}' отправлено с темой '{{ title }}'
    {% endif %}
{% endmacro %}