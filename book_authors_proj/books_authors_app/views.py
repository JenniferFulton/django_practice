from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, "index.html", context)

def create_book(request):
    if request.method == "POST":
        print(request.POST)
        Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        )
    return redirect('/')

def book_info(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        "book": book,
        "authors": Author.objects.exclude(books__id=book_id)
    }

    return render(request,'book_info.html', context)

def authors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, "auth.html", context)

def create_author(request):
    if request.method == "POST":
        Author.objects.create(
            first_name= request.POST['first_name'], 
            last_name= request.POST['last_name'], 
            notes = request.POST['notes']
        )
    return redirect('/authors')

def author_info(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "books": Book.objects.exclude(authors__id=author_id)
    }
    return render(request, "auth_info.html", context)



