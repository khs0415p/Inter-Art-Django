from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def address_process(value):
    value = str(value)
    value = value[value.rfind("/")+1:]
    return value