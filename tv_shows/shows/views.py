from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages

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
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('shows/new')
        else:
            Show.objects.create(
                title = request.POST['title'],
                network = request.POST['network'],
                release_date = request.POST['release_date'],
                description = request.POST['description']
            )
            messages.success(request, "New show successfully created!")
    return redirect('/shows')

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
        to_update = Show.objects.get(id=show_id)

        to_update.title = request.POST['title']
        to_update.network = request.POST['network']
        to_update.release_date = request.POST['release_date']
        to_update.description = request.POST['description']
        to_update.save()

        return redirect('/shows')

def delete_show(request, show_id):
    #Will delete a show and return to All Shows page
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')
    
