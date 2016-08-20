import markdown
from django import template

register = template.Library()

@register.filter
def markdownify(text):
    return markdown.markdown(text, extensions=["markdown.extensions.extra", "markdown.extensions.codehilite"] , safe_mode='escape')
