from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def results(request):
    return HttpResponse("results will show here")
