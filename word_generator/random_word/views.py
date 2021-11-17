from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def word(request):
    return HttpResponse('Random word will generate')

def reset(request):
    return HttpResponse('Will reset/redirect')
