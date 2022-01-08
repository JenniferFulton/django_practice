from django.shortcuts import render, redirect, HttpResponse
from .models import Shows

def root_route(request):
    #Will redirect to All shows page
    return redirect('/shows')

def all_shows(request):
    #Will have a table with All shows and the ability to 
    #add a new show which will be a link that redirects to /shows/new
    context = {
        "all_shows": Shows.objects.all()
    }
    return render(request, 'all_shows.html', context)

