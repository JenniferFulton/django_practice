from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, "index.html", context)

def create_book(request):
    return redirect('/')

# Need path for /books/<books.id>

def authors(request):
    context = {
        'all_authors': Author.objects.all()
    }
    return render(request, "auth.html", context)

def create_author(request):
    return redirect('/authors')

# Need path for /authors/<author.id>
