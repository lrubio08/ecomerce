from django import template

register = template.Library()


@register.filter
def clp(value):
    """Formatea un número como pesos chilenos: 699990 -> $699.990"""
    try:
        numero = round(value)
    except (TypeError, ValueError):
        return value
    return "$" + f"{numero:,}".replace(",", ".")