from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def results(request):
    print(request.POST)
    
    request.session['name'] = request.POST['name']
    request.session['gender'] = request.POST['gender']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['favorite language']
    request.session['color'] = request.POST['color']
    request.session['comments'] = request.POST['describe']
    return redirect('/success')

def success(request):
    return render(request, "results.html")

