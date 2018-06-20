from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse 

from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    STATUS_CHOICES = (
                      ('draft', 'Draft'),
                      ('published', 'Published'),
                     )
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    author = models.ForeignKey(to=User, 
                               on_delete=models.CASCADE, related_name='blog_posts')

    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', 
                        args=[self.publish.year, self.publish.month, self.publish.day, self.slug])



class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    
    
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


    class Meta:
        ordering = ('created', )

    

