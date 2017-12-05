from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth import login, authenticate, logout

from .models import Book, Author, Comment

from .forms import SignUpForm, SampleForm, CommentForm

def index(request):
    books = Book.objects.all()
    context = {"books": books}
    print(request.user)
    return render(request, "my_bookstore/index.html", context)

def book_page(request, book_id, title):
    book = get_object_or_404(Book, pk=book_id)
    form_errors = {}
    form_values = {"title": "", "body": "", "rating": 0}
    if request.POST:
        print("rating=", request.POST["rating"], type(request.POST["rating"]))
        print("comment=", request.POST["yorum"])
        form_values["title"] = request.POST["title"]
        form_values["body"] = request.POST["yorum"]
        form_values["rating"] = int(request.POST["rating"])
        if len(request.POST["yorum"]) < 10:
            form_errors["body"] = "You comment is too short. It should be at least 10 characters"
        if len(request.POST["title"]) == 0:
            form_errors["title"] = "Title field is required"
        if form_values["rating"] == 0:
            form_errors["rating"] = "Please select a rating"
        if len(form_errors) == 0:
            new_comment = Comment()
            new_comment.title = form_values["title"]
            new_comment.body = form_values["body"]
            new_comment.book = book
            new_comment.rating = form_values["rating"]
            new_comment.save()
            form_values["title"] = ""
            form_values["body"] = ""
            form_values["rating"] = 0
            print("SAVED")
    else: # page loaded first time. no form POST data
        pass
        # print(request.POST["yorum"])

    context = {"book": book, "errors": form_errors,
               "values": form_values}
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
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.bio = form.cleaned_data.get('bio')
            print("avatar", form.cleaned_data.get('avatar'))
            print(request.FILES)
            user.profile.avatar = request.FILES['avatar']
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'my_bookstore/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    # return redirect(request.path)
    return redirect("/")

def login_view(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass
    # return redirect(request.path)
    return redirect("/")


def test_forms(request):
    if (request.POST):
        form = SampleForm(request.POST)
        print(request.POST)
        form2 = CommentForm(request.POST)
        if form2.is_valid():
            form2.save()
    else:
        form = SampleForm()
        form2 = CommentForm()
    return render(request, 'my_bookstore/test_forms.html',
                    {'form': form, 'form2': form2}
                 )

    
    
    
    
