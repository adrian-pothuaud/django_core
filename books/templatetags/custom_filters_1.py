from django import template


register = template.Library()


@register.filter
def lower(value):
    return value.lower()


@register.filter
def better(value):
    return "%s+++" % value


@register.filter(is_safe=True)
def add_xxx(value):
    return 'xxx%sxx' % value
