from django.shortcuts import render, redirect

def root_route(request):
    redirect('/shows')

