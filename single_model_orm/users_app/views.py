from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Does this route work?")
