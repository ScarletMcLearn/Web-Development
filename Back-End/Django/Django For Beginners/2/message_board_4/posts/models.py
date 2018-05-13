from django.db import models

# Create your models here.
from django.utils import timezone       # For created, updated dates

class Post(models.Model):               # Post Model for DB
    text = models.TextField()
    category = models.CharField(max_length=150, null=True)      
    # CharField REQUIRES max_length
    # null is given cause DB previously populated with fields missing 

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # Created At, Updated At - DateTimeField Config #############
                                                                #
    created_at     = models.DateTimeField(editable=False,   auto_now_add=True)                                          #
    updated_at    = models.DateTimeField(auto_now=True)         #
                                                                #
    def save(self, *args, **kwargs):                            #
        ''' On save, update timestamps '''                      #
        if not self.id:                                         #
            self.created_at = timezone.now()                    #
        self.updated_at = timezone.now()                        #
        return super(Post, self).save(*args, **kwargs)          #
                                                                #
#################################################################

    def __str__(self):  # String representation of Model : Title / Label for Model / Object
        return self.text[:50]
