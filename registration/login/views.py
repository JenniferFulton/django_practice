from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

def registration_login(request):
    #root route will have a form for registration and form for logging in
    return render(request, 'reg_login.html')

def register(request):
    #'/register' will create a new user and redirect back to login page
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        
        else:
            User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = request.POST['password'],
            )
            messages.success(request, "Registration successful, proceeed to login!")
    return redirect('/')
