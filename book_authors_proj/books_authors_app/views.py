from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, "index.html", context)

def create_book(request):
    return redirect('/')
