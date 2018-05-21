from django.contrib import admin

# Register your models here.
from .models import *

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # pass
    list_display = ('title', 'author', 'display_genre',)
    inlines = [BooksInstanceInline]

class AuthorAdmin(admin.ModelAdmin):
    # pass
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death',)
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death'),]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)

# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # pass
    list_filter = ('status', 'due_back',)

    fieldsets = (
        (None, {'fields' : ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )
