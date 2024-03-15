from django import template


register = template.Library()


@register.filter()
def mymedia(val):
    """Тег для товаров"""
    if val:
        return f'/media/{val}'

    return '/media/product.jpeg'


@register.filter()
def forblog(val):
    """Тег для блогов"""
    if val:
        return f'/media/{val}'
