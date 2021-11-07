
# / - display the string "placeholder to later display a list of all blogs" with a method named "index"
# /new - display the string "placeholder to display a new form to create a new blog" with a method named "new"
# /create - redirect to the "/" route with a method called "create"
# /int:number - display the string "placeholder to display blog number: {number}" with a method named "show" (eg. localhost:8000/15 should display the message: 'placeholder to display blog number 15')
# /int:number/edit - display the string "placeholder to edit blog {number}" with a method named "edit"
# /int:number/delete - redirect to the "/" route with a method called "destroy"

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return index(request)

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")