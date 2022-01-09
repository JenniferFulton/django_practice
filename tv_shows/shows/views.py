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
    #A form will show that will allow the user to crete a new show
    #or go back to all shows page
    return render(request, 'new_show.html')

def create (request):
    #When the user submits a new show
    if request.method == "POST":
        Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description']
        )
    return redirect('/shows/<int:show_id>')

def show_info(request, show_id):
    #This page will show the details of a speicific show
    context = {
        "show": Show.objects.get(id=show_id)
    }
    return render(request, 'show_info.html', context)

def edit_show(request, show_id):
    context = {
        'update_show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit_show.html', context)

    
    
def update_show_info(request, show_id):    
    #will allow you to edit a show's details and return back to show's info page
    if request.method == "POST":
        update_show = Show.objects.get(id=show_id)

        update_show.title = request.POST['title'],
        update_show.network = request.POST['network'],
        update_show.release_date = request.POST['release_date'],
        update_show.description = request.POST['description']
        
        update_show.save()
        return redirect('/shows/<int:show_id>')

def delete_show(request, show_id):
    #Will delete a show and return to All Shows page
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')
    
