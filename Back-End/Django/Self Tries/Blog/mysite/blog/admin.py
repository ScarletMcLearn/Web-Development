from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Post)

admin.site.register(Comment)

from blog.models import *


class CommentInline(admin.TabularInline):
    model = Comment

    readonly_fields = ('commented_date', )
    fieldsets = [
        ('Comment',               {'fields': ['body', readonly_fields]}),
        # ('Date information', {'fields': readonly_fields}),
    ]

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag_list', 'published_date', 'edited_date', ]
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    readonly_fields = ('published_date', 'edited_date', 'slug')
    fieldsets = [
        ('Post',               {'fields': ['title', readonly_fields[2], 'body', 'tags', ]}),
        ('Date information', {'fields': readonly_fields[:2]}),
    ]

    inlines = [
        CommentInline,
    ]

admin.site.register(Post, PostAdmin)
