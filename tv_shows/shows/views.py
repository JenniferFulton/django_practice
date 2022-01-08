from django.shortcuts import render, redirect, HttpResponse

def root_route(request):
    return redirect('/shows')

def all_shows(request):
    return HttpResponse("You got here from root redirect")

