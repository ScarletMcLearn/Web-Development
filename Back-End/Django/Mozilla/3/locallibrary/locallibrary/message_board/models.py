from django.db import models

# Create your models here.
from django.urls import reverse
# from datetime import date

# from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Notice(models.Model):
    notice_title = models.CharField(max_length=200, help_text='Enter a title for the notice (e.g. Make-Up Class.)')
    notice_text = models.TextField(help_text='Enter a description for the notice.')
    published_date = models.DateField(verbose_name='Published on', null=True, blank=True)
    event_date = models.DateField(verbose_name='Takes place on', null=True, blank=True)

    # posted_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True,)Group
    posted_by = models.ForeignKey(to=Group, on_delete=models.SET_NULL, null=True,)

    EVENT_OPTIONS = (
        ('t', 'Tests Week'),
        ('m', 'Mid Term Examinations'),
        ('f', 'Final Examinations'),
        ('s', 'Seminar'),
        ('w', 'Workshop'),
        ('h', 'Holiday'),
        ('m', 'Make-Up Class'),
        ('n', 'Notice'),
    )

    

    event_kind = models.CharField(max_length=1, choices=EVENT_OPTIONS, default='n', blank=True, help_text='Notice Type')

    

    def __str__(self):
        return self.notice_title

    def get_absolute_url(self):
        return reverse(viewname='notice-detail', args=[str(self.id)])

    class Meta:
        ordering = ['event_date']