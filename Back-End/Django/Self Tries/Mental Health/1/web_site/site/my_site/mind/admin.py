from django.contrib import admin

# Register your models here.
from . import models

# class TaggedTextAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(models.TaggedText, TaggedTextAdmin)

# class AuthorAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(models.Author, AuthorAdmin)


# class CategoryAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(models.Category, CategoryAdmin)


# class ArticleAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(models.Article, ArticleAdmin)


# class ImageAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(models.Image, ImageAdmin)


# class AMA_ArticleAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(models.AMA_Article, AMA_ArticleAdmin)# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Author, ArticleInfo, Tag, ImgUrl, TaggedText


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(ArticleInfo)
class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'published_status',
        'source_link',
        'posted_on',
        'author',
        'credit',
        'content',
    )
    list_filter = ('published_status', 'posted_on', 'author')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'article')
    list_filter = ('article',)


@admin.register(ImgUrl)
class ImgUrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'article')
    list_filter = ('article',)


@admin.register(TaggedText)
class TaggedTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'c_tag', 'article')
    list_filter = ('article',)
