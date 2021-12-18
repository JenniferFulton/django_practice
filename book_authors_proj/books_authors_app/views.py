from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    return render(request, "index.html")

def create_book(request):
    return redirect('/')
