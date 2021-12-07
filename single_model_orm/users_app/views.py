from django.shortcuts import render, redirect
from .models import User

def index(request):
    context = {
        "all_users": User.objects.all(),
    }
    return render(request, "index.html", context)

def create(request):
    
    return redirect("/")
