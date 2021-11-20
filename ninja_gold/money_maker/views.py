from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, 'index.html')

def process(request):

    request.session[activities] = []
    return redirect(request, '/')
