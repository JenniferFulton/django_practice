from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def results(request):
    print(request.POST)
    
    request.session["Name"] = request.POST['name']
    request.session["Gender"] = request.POST['gender']
    request.session["Location"] = request.POST['location']
    request.session["Language"] = request.POST['favorite language']
    request.session["Color"] = request.POST['color']
    request.session["Comments"] = request.POST['describe']

    return redirect('/')


