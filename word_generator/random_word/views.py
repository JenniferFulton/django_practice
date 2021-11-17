from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Testing, Testing 1,2,3...")
