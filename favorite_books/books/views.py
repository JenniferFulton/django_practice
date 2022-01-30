from multiprocessing import context
from select import select
from django.shortcuts import render, redirect
from login.models import *
from .models import *
from django.contrib import messages

def home_page(request):
    #Checks if user is logged in
    if 'user' not in request.session:
        return redirect('/')
    
    #will be redirected to home page once logged in or registered
    active_user = User.objects.get(id = request.session['user'])
    context = {
        'user' : active_user,
        'all_books' : Book.objects.all(),
    }
    return render(request, 'books_home.html', context)

def create_book(request):
#Checks if user is logged in
    if 'user' not in request.session:
        return redirect('/')
    else:
        if request.method == "POST":
            errors = Book.objects.book_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/books')
            
            else:
                Book.objects.create(
                    title = request.POST['title'],
                    description = request.POST['description'],
                )
                return redirect('/books')

def book_info(request, id):
    active_user = User.objects.get(id = request.session['user'])
    selected_book = Book.objects.get(id=id)

    context = {
        'book': selected_book,
        'user' : active_user,
    }
    return render(request, 'book_info.html', context)



