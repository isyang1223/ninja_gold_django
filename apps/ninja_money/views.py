from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, localtime
import random
def index(request):
    if 'gold' in request.session:
        request.session['gold'] = request.session['gold']
    else:
        request.session['gold'] = 0
    

    
    return render(request,'ninja_money/index.html')

def process_money(request):
    if not "message" in request.session:
        request.session["message"] = []
        

    if request.POST["building"] == "farm":
        earned = random.randrange(10,21)
        request.session['gold'] += earned
        request.session["message"].append("Earned " + str(earned) + " golds from the farm! ("+strftime('%I:%M %p %a %m-%d-%Y',localtime())+")")

    elif request.POST["building"] == "cave":
        earned = random.randrange(5,11)
        request.session['gold'] += earned
        request.session["message"].append("Earned " + str(earned) + " golds from the cave! ("+strftime('%I:%M %p %a %m-%d-%Y',localtime())+")")

    elif request.POST["building"] == "house":
        earned = random.randrange(2,6)
        request.session['gold'] += earned
        request.session["message"].append("Earned " + str(earned) + " golds from the house! ("+strftime('%I:%M %p %a %m-%d-%Y',localtime())+")")

    elif request.POST["building"] == "casino":
        earned = random.randrange(-50,51)
        request.session['gold'] += earned
        if earned > 0:
            request.session["message"].append("Earned " + str(earned) + " golds from the casino! ("+strftime('%I:%M %p %a %m-%d-%Y',localtime())+")")
        else:
            request.session["message"].append("Entered a casino and lost " + str(abs(earned)) + " golds... Ouch.. ("+strftime('%I:%M %p %a %m-%d-%Y',localtime())+")")
    
    return redirect('/')


def reset(request):
    # if request.method == "POST":
    request.session['gold'] = 0
    request.session["message"] = []



    return redirect('/')