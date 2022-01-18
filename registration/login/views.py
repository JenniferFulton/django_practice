from django.shortcuts import render, redirect

def registration_login(request):
    #root route will have a form for registration and form for logging in
    return render(request, 'reg_login.html')

def register(request):
    #'/register' will create a new user and redirect back to login page
    return redirect('/')
