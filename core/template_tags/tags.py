from django import template

register = template.Library()


@register.filter
def build_uri_no_query(request):
    return request.build_absolute_uri(request.path)
