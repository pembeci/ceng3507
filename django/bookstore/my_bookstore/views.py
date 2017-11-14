from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Book

def index(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "my_bookstore/index.html", context)

def book_page(request, book_id, title):
    print(book_id, title)
    book = get_object_or_404(Book, pk=book_id)
    context = {"book": book}
    return render(request, "my_bookstore/book.html", context)

def cat_page(request, cat):

    category = Book.genre_dict[cat]
    print("cat: |{}|".format(category))
    books = Book.objects.all().filter(genre=category)
    print("books", books)
    context = {"books": books, "cat_name": cat}
    return render(request, "my_bookstore/index.html", context)