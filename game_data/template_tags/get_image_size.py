from django import template

register = template.Library()


@register.filter
def get_image_size(obj, size):
    try:
        return obj.get_image(size=size)
    except:
        return ''

@register.filter
def get_portrait_size(obj, size):
    try:
        return obj.get_portrait(size=size)
    except:
        return ''
