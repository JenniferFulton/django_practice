from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        'all_dojos': Dojo.objects.all(),
        'all_ninjas': Ninja.objects.all(),
    }
    return render(request, "index.html", context)
