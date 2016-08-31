from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from .sitemap import BlogSitemap
from blog.models import Entry


info_dict = {
            'queryset' : Entry.objects.all(),
            'date_field' : 'modified',
        }

urlpatterns = [
    # Examples:
    # url(r'^$', 'MySite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'blog/', include('blog.urls', namespace='blog')),
    url(r'^$', include('blog.urls', namespace='blog')),

    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps' : {'blog' : GenericSitemap(info_dict, priority=0.5, changefreq="monthly")} },
        name='django.contrib.sitemaps.views.sitemap'
    ),
]
