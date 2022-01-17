from django.shortcuts import render, HttpResponse

def index(request):
    #root route will take you to page where you can add a new course, and a table
    #with the list of classes, where you will be able to remove  class
    return HttpResponse('Testing the root route')
