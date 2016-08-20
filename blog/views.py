from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django import template

from django.contrib.syndication.views import Feed
from django.contrib import sitemaps

from blog.models import *

import re
import markdown

from itertools import chain, combinations, permutations

item_per_page = 5

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(permutations(s,r) for r in range(len(s) + 1))

def getSubsetList(iterable):
    c = powerset(iterable)
    return [ list(x) for x in c]

def paginate(request, result_list,  per_page):
    paginator = Paginator(result_list, per_page)
    page = request.GET.get("page")
    results = []
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
            results = paginator.page(paginator.num_pages)
    return results

class BlogIndex(View):

    def get(self,request):
        context = {}
        entry_list = Entry.objects.all()
        context['entries'] = entry_list
        context['entries_paginated'] = paginate(request, entry_list,  item_per_page)
        return render(request, 'blog/index.html', context)

class EntryDetail(View):

    def get(self,request, slug):
        context = {}
        entry = get_object_or_404(Entry, slug=slug)
        comments = Comment.objects.filter(entry=entry)
        context['entry'] = entry
        context['comments'] = comments
        return render(request, 'blog/detail.html', context)

    def post(self, request, slug):
        entryid = request.POST.get('entryid')
        commenter = request.POST.get('commenter','')
        body = request.POST.get('body','').strip()
        if body:
            entry = get_object_or_404(Entry, id=entryid)
            comment = Comment(commenter=commenter, entry=entry, body=body)
            comment.save()
            return HttpResponseRedirect('/blog/detail/'+slug)

class EntrySearch(View):

    def get(self, request):
        context = {}
        querystring = request.GET.get('query','').strip()
        query = Q()
        if not querystring:
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            querystring = querystring.lower()
            # split according to spaces
            query_list = re.split(r'\s+', querystring)
            temp = [ re.escape(string) for string in query_list]
            query_list = list(set(temp))

            '''
            # get possible words
            words_combinations = getSubsetList(query_list)
            word_list = []
            for x in words_combinations:
                if len(x)>0:
                    word_list.append(' '.join(x))
            '''

            regexstring = r'(' + '|' .join(query_list) + ')'

            #print(query_list)

            entry_list = []
            '''
            for tagstr in query_list:
                tagobj= Tag.objects.filter(title=tagstr)
                if tagobj:
                    entryobj = Entry.objects.filter(tags = tagobj)
                    entry_list += entryobj

            entry_list = list(set(entry_list))
            entry_list = sorted(entry_list, key=lambda x: x.created, reverse=True)
            '''

            title_list= Entry.objects.filter(title__iregex=regexstring).distinct()
            tag_list= Entry.objects.filter(tags__title__iregex = regexstring).distinct()

            from itertools import chain
            entry_list = list(set(chain(title_list, tag_list)))
            entry_list = sorted(entry_list, key=lambda x: x.created, reverse=True)

            context['querystring'] = querystring
            context['query'] = querystring
            context['entries'] = entry_list
            context['entries_paginated'] = paginate(request, entry_list, item_per_page)
            context['title_list'] = title_list
            context['tag_list'] = tag_list
            return render(request, 'blog/searchresults.html', context) 

    def post(self, request):
        return HttpResponse("hello")

class About(View):

    def get(self, request):
        context = {}
        about_file = open("blog/markdownfiles/about.md", 'r')
        about_text = about_file.read()
        context['about'] = about_text
        about_file.close()
        return render(request, 'blog/about.html', context)

class LatestEntriesFeed(Feed):
    title = "CodingParadox blog post"
    link = "/blog/"
    description = "updates on latest blogs"
    feed_copyright = "Copyright @ Nishan Pantha"
    feed_url = "/blog/rss"

    def items(self):
        return Entry.objects.order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        return markdown.markdown(item.body, safe_mode='escape')

class MarkdownTest(View):

    def get(self, request):
        context = {}
        markdowntest_file = open("blog/markdownfiles/markdowntest.md", 'r')
        markdowntest_text = markdowntest_file.read()
        context['markdowntest'] = markdowntest_text
        markdowntest_file.close()
        return render(request, 'blog/markdowntest.html', context)









