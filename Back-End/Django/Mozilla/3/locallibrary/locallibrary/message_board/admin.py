from django.contrib import admin

# Register your models here.
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    # pass
    list_display = ('notice_title', 'event_kind', 'published_date', 'event_date')
    # inlines = [BookInstanceInline]