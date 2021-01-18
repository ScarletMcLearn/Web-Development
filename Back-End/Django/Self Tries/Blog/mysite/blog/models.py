from django.db import models

from datetime import datetime, timedelta


from django.utils.text import slugify 

from taggit.managers import TaggableManager


def generate_unique_slug(klass, field):
    """
    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`

    :param `klass` is Class model.
    :param `field` is specific field for title.
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 2
    while klass.objects.filter(slug=unique_slug).exists():
        # if numb == 1:
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_date = models.DateTimeField("Date Published", auto_now=False, auto_now_add=True, editable=False)
    edited_date = models.DateTimeField("Date Edited", auto_now=False, auto_now_add=True, editable=False)
    slug = models.SlugField(unique=True, editable=False)

    tags = TaggableManager(verbose_name="Tags", help_text="A comma-separated list of tags.")



    def __str__(self):
        return self.title


    def was_published_recently(self):
        return self.published_date >= datetime.now() - timedelta(days=30)

    def was_edited_recently(self):
        return self.published_date >= datetime.today() - timedelta(days=7)

    
    
    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)

        if self.slug:  # edit
            if slugify(self.title.lower()) != self.slug:
                self.slug = generate_unique_slug(Post, self.title.lower())
        else:  # create
            self.slug = generate_unique_slug(Post, self.title.lower())




        if self.published_date is None:
            self.published_date = datetime.today()
        else:
            self.edited_date = datetime.today()
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    # votes = models.IntegerField(default=0)


    # TO DO - FIX COMMENT DATE - EDIT DATE - DONE
    commented_date = models.DateField("Date Commented", auto_now_add=True, editable=False)
    # edited_date = models.DateField("Date Edited", auto_now=False, auto_now_add=True, editable=False)

    def save(self, *args, **kwargs):
        # if self.commented_date is None:
        #     self.commented_date = date.today()
        # else:
        #     self.edited_date = date.today()
        self.commented_date = datetime.today()
        super(Comment, self).save(*args, **kwargs)


    def __str__(self):
        return self.body[:50]


    def was_commented_recently(self):
        return self.commented_date >= datetime.today() - timedelta(days=3)




# from blog.models import *
# p = Post(title='TP')

