from django import template

register = template.Library()

@register.simple_tag
def percentage(a, b):
    result = a / b
    result = round(result*100, 1)
    return result