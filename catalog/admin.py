from django.contrib import admin
from.models import Book, Author, BookInstance, Language, Genre, CreateUser

# Register your models here.

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(CreateUser)


class BooksInLine(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):  # Define the admin class
    list_display = ('last_name', 'first_name', 'Date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('Date_of_birth', 'date_of_death')]
    inlines = [BooksInLine]


admin.site.register(Author, AuthorAdmin)  # Register the admin class with the associated model


class BooksInstanceInLine(admin.TabularInline):
    model = BookInstance


@admin.register(Book)  # Register the Admin classes for Book using the decorator
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'summary', 'display_genre')
    inlines = [BooksInstanceInLine]


@admin.register(BookInstance)  # Register the Admin classes for BookInstance using the decorator
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'imprint', 'due_back', 'status', 'borrower')
    list_filter = ('status', 'due_back')  # Creates a filter box at the side in admin

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
