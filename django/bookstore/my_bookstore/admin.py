from django.contrib import admin

from .models import Book, Author, Profile, Comment



class BookAdmin(admin.ModelAdmin):
  model = Book
  list_display = ['title', 'genre']

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
  model = Author
  list_display = ['id', 'name']

admin.site.register(Author, AuthorAdmin)

class ProfileAdmin(admin.ModelAdmin):
  model = Profile
  # list_display = ['id', 'name']

admin.site.register(Profile, ProfileAdmin)

class CommentAdmin(admin.ModelAdmin):
  model = Comment
  list_display = ['title', 'book', 'rating']

admin.site.register(Comment, CommentAdmin)
