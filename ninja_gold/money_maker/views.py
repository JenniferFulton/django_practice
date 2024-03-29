from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    return render(request, 'index.html')

def process(request):
    if request.method == 'POST':
        print(request.POST)
        time = strftime("%B %d, %Y %I:%M %p", gmtime())
    
        if 'activities' not in request.session:
            request.session['activities'] = []

        if "gold" not in request.session:
            request.session["gold"]= 0
    
        else:
            if request.POST['place']== 'farm':
                farm_gold = random.randint(10, 20)
                request.session["gold"] += farm_gold
                request.session['activities'].append(f"Earned {farm_gold} from the farm! {time}")

            if request.POST['place']== 'cave':
                cave_gold = random.randint(5, 10)
                request.session["gold"] += cave_gold
                request.session['activities'].append(f"Earned {cave_gold} from the cave! {time}")  

            if request.POST['place']== 'house':
                house_gold = random.randint(2, 5)
                request.session["gold"] += house_gold
                request.session['activities'].append(f"Earned {house_gold} from the house! {time}")   

            if request.POST['place']== 'casino':
                casino_gold = random.randint(-50, 50)
                request.session["gold"] += casino_gold
                if casino_gold < 0:
                    request.session['activities'].append(f"Lost {casino_gold} from the casino...OUCH! {time}")
                else:
                    request.session['activities'].append(f"Earned {casino_gold} from the casino! {time}")

        return redirect('/')