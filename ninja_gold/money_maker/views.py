from django.shortcuts import render, redirect
import random
import time 

def index(request):
    gold = 0
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        print(request.POST)
        activities = []
        if "gold" not in request.session:
            request.session["gold"]= 0

        if request.POST['place']== 'farm':
            farm_gold = random.randint(10, 20)
            request.session["gold"] += farm_gold
            activities.append(f"Earned {farm_gold} from the farm!")

        if request.POST['place']== 'cave':
            cave_gold = random.randint(5, 10)
            request.session["gold"] += cave_gold
            activities.append(f"Earned {cave_gold} from the cave!")  

        if request.POST['place']== 'house':
            house_gold = random.randint(2, 5)
            request.session["gold"] += house_gold
            activities.append(f"Earned {house_gold} from the house!")   

        if request.POST['place']== 'casino':
            casino_gold = random.randint(-50, 50)
            request.session["gold"] += casino_gold
            if casino_gold < 0:
                activities.append(f"Lost {casino_gold} from the casino...OUCH!")
            else:
                activities.append(f"Earned {casino_gold} from the casino!")
        
        if 'activities' not in request.session:
            request.session['activities'] = []
        else:
            request.session['activities'] += activities

        return redirect('/')