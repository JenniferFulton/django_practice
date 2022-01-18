from django.shortcuts import render

def registration_login(request):
    return render(request, 'reg_login.html')
