from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse('Testing the route')

def test(request):
    return HttpResponse("testing a different route")
