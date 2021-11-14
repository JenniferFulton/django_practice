from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("what's up")

def results(request):
    return HttpResponse("results will show here")
