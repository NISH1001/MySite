from django import template

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

register = template.Library()

@register.filter
def encodeurl(querytext):
    query_dict = {"query" : querytext}
    encoded = urlencode(query_dict)
    return encoded[6::]
