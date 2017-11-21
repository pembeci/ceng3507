from django.contrib import admin

from .models import Book, Author



class BookAdmin(admin.ModelAdmin):
  model = Book
  list_display = ['title', 'genre']

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
  model = Author
  list_display = ['id', 'name']

admin.site.register(Author, AuthorAdmin)
