from django import template

register = template.Library()


@register.filter(name="euros")
def euros(value):
    return f"{value / 100:.2f} €".replace(".", ",")
