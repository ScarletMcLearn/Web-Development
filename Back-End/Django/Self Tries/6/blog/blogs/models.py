from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE, help_text='Author of Post', verbose_name='author name')
    title = models.CharField(max_length=200, help_text='Please enter Title of Post', verbose_name='post title', blank=False, null=False)
    body = models.TextField(help_text='Please enter Body of Post', verbose_name='post body', blank=True, null=True)
    slug = models.SlugField(max_length=40, allow_unicode=True, unique=True)
    created_date = models.DateTimeField(verbose_name='created ', editable=False, auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    image = models.ImageField(upload_to='post image', blank=True, null=True)
    local_view_count = models.IntegerField(editable=False, default=0,)
    global_view_count = models.IntegerField(editable=False, default=0,)

    def increment_local_count(self):
        self.local_view_count = self.local_view_count + 1
        # print(self.local_view_count)
        return 

    def increment_global_count(self):
        self.global_view_count = self.global_view_count + 1
        # print(self.global_view_count)
        return 

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_date = timezone.now()
    #     self.updated_date = timezone.now()
    #     return super(User, self).save(*args, **kwargs)



