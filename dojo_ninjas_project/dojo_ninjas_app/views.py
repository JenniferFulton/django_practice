from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("just practicing my routing!")
