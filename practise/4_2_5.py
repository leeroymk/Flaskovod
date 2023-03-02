<form action="" method="POST">

{{ form.csrf_token() }}
{% for field in form if field.name not in ["csrf_token", "submit"] %}
    {{ field.label() }}
        {{ field }}
        {% for error in field.errors %}
        {{ error }}
        {% endfor %}
{% endfor %}
{{ form.submit() }}

</form>
