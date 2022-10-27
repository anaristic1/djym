from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='search')
@stringfilter
def url_search(value):
    return f"https://www.youtube.com/results?search_query={value.replace(' ', '+')}"
