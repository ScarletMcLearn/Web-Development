from django.contrib import admin

# Register your models here.
from .models import Book, BookInstance, Genre, Author

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # pass
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    search_fields = ['first_name', 'last_name', ]

admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # pass
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # pass
    list_filter = ('status', 'borrower', 'due_back')
    search_fields = ['book__title', ]       # search field using foreign key
    
    fieldsets =(
        (None, 
            {
            'fields': ('book', 'imprint', 'id')
            }
        ),
        ('Availability', 
            {
            'fields': ('status', 'due_back', 'borrower')
            }
        ),
    )

admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(BookInstance)