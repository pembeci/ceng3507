from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Book, Author

from .forms import SignUpForm

def index(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "my_bookstore/index.html", context)

def book_page(request, book_id, title):
    print(book_id, title)
    book = get_object_or_404(Book, pk=book_id)

    context = {"book": book}
    return render(request, "my_bookstore/book.html", context)

def author_page(request, author_id, author):
    
    author = get_object_or_404(Author, pk=author_id)

    context = {"author": author}
    print(author.book_set.all())
    return render(request, "my_bookstore/author.html", context)
    
def cat_page(request, cat):

    cat = cat.capitalize()
    category = Book.genre_dict.get(cat, "")    
    print("cat: |{}|".format(category))
    books = Book.objects.all().filter(genre=category)
    print("books", books)
    context = {"books": books, "cat_name": cat }
    return render(request, "my_bookstore/category.html", context)
    
# user account views

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            # user.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'my_bookstore/signup.html', {'form': form})
    
    
    
    
    
    
