from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def registration_login(request):
    #root route will have a form for registration and form for logging in
    return render(request, 'reg_login.html')

def register(request):
    #'/register' will create a new user and redirect back to login page
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = hashed_pw,
            )
            messages.success(request, "Registration successful, proceeed to login!")
        return redirect('/')

def login(request):
    #'/login' will verify email and password to allow user to login
    #if no errors return redirect('/success')
    #if errors return redirect('/')

def success(request):
    #'/success' will allow user to be at their homepage once they are logged in
    return render(request, 'login_success.html')
