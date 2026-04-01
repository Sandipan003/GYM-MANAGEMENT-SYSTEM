from django import template

register = template.Library()


@register.filter
def split(string, separator=','):
    """Split a string by separator"""
    if not string:
        return []
    return [item.strip() for item in string.split(separator)]


@register.filter
def trim(string):
    """Trim whitespace from a string"""
    if not string:
        return ''
    return string.strip()
