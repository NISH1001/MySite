from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'MySite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^detail/(?P<slug>\S+)$', views.EntryDetail.as_view(), name="entry_detail"),
    url(r'^search/$', views.EntrySearch.as_view(), name="entry_search"),
    url(r'^about/$', views.About.as_view(), name="about"),
    url(r'^rss/$', views.LatestEntriesFeed(), name="rss"),
    url(r'^markdowntest/$', views.MarkdownTest.as_view(), name="markdowntest"),
]
