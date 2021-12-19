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

# Need path for /books/<books.id>

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

# Need path for /authors/<author.id>
