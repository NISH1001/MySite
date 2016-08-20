from django.db import models

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Entry(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/detail/%s" % self.slug

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ['-created']

class Comment(models.Model):
    commenter = models.CharField(max_length=50)
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    entry = models.ForeignKey('Entry')

    def __str__(self):
        return self.commenter+" --" + self.entry.title
