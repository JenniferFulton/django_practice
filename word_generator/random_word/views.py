from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "index.html")

def word(request):
    context = {
        'word': get_random_string(length=14)
    }
    return render(request, "random_word.html", context,)


