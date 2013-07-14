from django import template

register = template.Library()


@register.filter
def normalize(value):
    return value.replace('_', ' ').title()