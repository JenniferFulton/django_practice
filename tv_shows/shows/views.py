from django.shortcuts import render, redirect, HttpResponse
from .models import Show

def root_route(request):
    #Will redirect to All shows page
    return redirect('/shows')

def all_shows(request):
    #Will have a table with All shows and the ability to 
    #add a new show which will be a link that redirects to /shows/new
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def new_show(request):
    return render(request, 'new_show.html')

def create (request):
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect('/shows/<int:show_id>')

def show_info(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id)
    }

    return render(request, 'show_info.html', context)