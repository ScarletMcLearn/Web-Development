# from django.contrib import admin
# from .models import Post
#
# admin.site.register(Post)


from django.contrib import admin
from blog.models import Post



class YourModelAdmin(admin.ModelAdmin):
    fields = ['author',
    'title' ,
    'text'
    'created_date' ,
    'published_date' ]



admin.site.register(Post, YourModelAdmin)
