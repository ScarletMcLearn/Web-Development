from django.db import models

# # Create your models here.

# class TaggedText(models.Model):
#     content = models.TextField(null=True, blank=True,)
#     text_tag = models.CharField(max_length=100, null=True, blank=True,)

#     def __str__(self):
#         return self.text_tag + ' : ' + self.content


# class Author(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True,)

#     def __str__(self):
#         return self.name


# class Category(models.Model):
#     category = models.CharField(max_length=100, null=True, blank=True,)

#     def __str__(self):
#         return self.category


# class Article(models.Model):
#     title = models.CharField(max_length=200, null=True, blank=True,)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True,)
#     source_url = models.URLField(null=True, blank=True,)
#     source = models.CharField(max_length=200, null=True, blank=True)
#     published_status = models.BooleanField(null=True, blank=True,)
 
#     credits = models.TextField(null=True, blank=True,)
#     category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.title


# class Image(models.Model):
#     image_url = models.URLField(null=True, blank=True,)

#     def __str__(self):
#         return self.image_url


# class AMA_Article(models.Model):
#     article = models.OneToOneField(
#         Article,
#         on_delete=models.CASCADE,
#          blank=True, null=True
#     )

#     contents = models.ForeignKey(TaggedText, null=True, blank=True, on_delete=models.SET_NULL)
#     img_url = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)

#     # posted_date = DateTimeField(default=datetime.datetime.now)
    
#     # def __str__(self):
#     #     return self.contents.TaggedText.contents





class Author(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.first_name + self.last_name



class ArticleInfo(models.Model):
    title = models.CharField(max_length=150)
    published_status = models.BooleanField(default=False)
    source_link = models.URLField(blank=True, null=True)
    posted_on = models.DateField(blank=True, null=True)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    credit = models.TextField(blank=True, null=True)

    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title



class Tag(models.Model):
    tag = models.CharField(max_length=150)
    article = models.ForeignKey(ArticleInfo, on_delete=models.CASCADE, 	blank=True, null=True)

    def __str__(self):
        return self.tag

class ImgUrl(models.Model):
    url = models.URLField()
    article = models.ForeignKey(ArticleInfo, on_delete=models.CASCADE, blank=True, null=True)

    img_style = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.url


class TaggedText(models.Model):
    content = models.TextField(blank=True, null=True)
    c_tag = models.CharField(max_length=20)
    article = models.ForeignKey(ArticleInfo, blank=True, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.c_tag + ' : ' + self.content    