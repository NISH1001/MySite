from django.contrib import admin
from blog.models import *

class TagInline(admin.StackedInline):
    model = Entry.tags.through
    extra = 3

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {'slug' : ('title',)}
    search_fields = ['title', 'tags__title']
    filter_horizontal = ['tags']
    #inlines = [TagInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ("commenter", "posted", "entry")
    search_fields = ['commenter', 'body']

admin.site.register(Tag)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment, CommentAdmin)

