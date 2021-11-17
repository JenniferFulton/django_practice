from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    word = get_random_string(length=14)
    
    context = {
        'word': word
    }
    return render(request, "index.html", context)

def word(request):
    return HttpResponse('Random word will generate')

def reset(request):
    return HttpResponse('Will reset/redirect')
