from django import template
import random

register = template.Library()

@register.filter
def shuffle(arg):
    tmp = list(arg)[:]
    random.shuffle(tmp)
    return tmp
