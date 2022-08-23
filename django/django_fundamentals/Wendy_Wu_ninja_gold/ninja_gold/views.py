from django.shortcuts import render, redirect
from datetime import datetime
from pytz import timezone
import random, pytz

def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    context = {
        "activities":request.session['activities']
    }
    return render(request, 'index.html', context)

def process_money(request):
    if request.method == 'POST':
        mygold= request.session['gold']
        activities = request.session['activities']
        location = request.POST['location']
        
        if location == 'farm':
            numbers = round(random.random() * 10+10)
        elif location == 'cave':
            numbers = round(random.random() * 5+5)
        elif location == 'house':
            numbers = round(random.random() * 3+2)
        else:
            winOrLose = round(random.random())
            if winOrLose == 1:
                numbers = round(random.random() * 50)
            else:
                numbers = (round(random.random() * 50)) * -1

            
        date_format = '%m%d%Y %h:%m:%s %z'
        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Pacific'))
        myTime = date.strftime(date_format)
            
        mygold+=numbers
        request.session['gold'] = mygold

        if numbers >= 0:
            str = f"Earn {numbers} from the {location} Yes!! {myTime}"
        else:
            numbers *= -1
            str = f"Lost {numbers} from the {location} Oh no... {myTime}"
        activities.insert(0, str)
        request.session['activities'] = activities
    return redirect('/')


