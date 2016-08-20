from blog.models import *
from django.db.models import Count
from math import log 

def calculateFonts(taglist):
    largest = taglist[0].num_entries
    smallest = taglist[len(taglist)-1].num_entries
    minimum = 1.0
    maximum = 2.5
    fontlist = []
    for tag in taglist:
        font = 0.8
        try:
            if tag.num_entries>0:
                font = log(tag.num_entries)/log(largest) * (maximum-minimum) + minimum
        except ZeroDivisionError:
            font = 0.8
        fontlist.append(font)
    return fontlist

def global_vars(request):
    context = {}
    entries = Entry.objects.all()
    context['global_entries'] = entries
    tags = Tag.objects.annotate(num_entries=Count('entry')).order_by('-num_entries')
    templist = {}
    temp = calculateFonts(tags)
    for index, scale in enumerate(temp):
        templist[tags[index].title] = scale
    context['tagcloud'] = templist
    return context
