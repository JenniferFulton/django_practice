from django.http.response import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def results(request):
    print(request.POST)
    context = {
        "Name": request.POST['name'],
        "Gender": request.POST['gender'],
        "Location": request.POST['location'],
        "Language": request.POST['favorite language'],
        "Color": request.POST['color'],
        "Comments": request.POST['describe'],
    }
    return render(request, "results.html", context)


