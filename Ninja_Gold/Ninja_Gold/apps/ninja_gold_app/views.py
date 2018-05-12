from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

def index(request):
    if 'gold_counter' not in request.session:
        request.session['gold_counter'] = 0
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []

    return render(request, 'ninja_gold_templates/index.html')

def process_money(request):
    building = request.POST['building']
    if 'gold_transfer' not in request.session:
        request.session['gold_transfer'] = 0
    if 'color_switch' in request.session:
        request.session.pop('color_switch')
        
    if building == 'farm':
        random_gold = random.randrange(10, 21)
        request.session['gold_transfer'] = random_gold
        log = {
            'message': ('Earned ' + str(request.session['gold_transfer']) + ' from the ' + building + ' (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')'),
            'color': 'green'
        }
        request.session['activity_log'].append(log)
    elif building == 'cave':
        random_gold = random.randrange(5, 11)
        request.session['gold_transfer'] = random_gold
        log = { 
            'message': ('Earned ' + str(request.session['gold_transfer']) + ' from the ' + building + ' (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')'),
            'color': 'green'
        }
        request.session['activity_log'].append(log)
    elif building == 'house':
        random_gold = random.randrange(2, 6)
        request.session['gold_transfer'] = random_gold
        log = {
            'message': ('Earned ' + str(request.session['gold_transfer']) + ' from the ' + building + ' (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')'),
            'color': 'green'
        }
        request.session['activity_log'].append(log)
    elif building == 'casino':
        random_gold = random.randrange(0, 51)
        random_test = random.randrange(0,2)
        if random_test == 1:
            request.session['gold_transfer'] = random_gold * -1
            log = {
                'message': ('Entered a casino and lost ' + str(request.session['gold_transfer'] * -1) + ' golds... Ouch.. ' +' (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')'),
                'color': 'red'
            }
            request.session['activity_log'].append(log)
        else:
            request.session['gold_transfer'] = random_gold
            log = {
                'message': ('Earned ' + str(request.session['gold_transfer']) + ' from the ' + building + ' (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')'),
                'color': 'green'
            }
            request.session['activity_log'].append(log)
    request.session['gold_counter'] += request.session['gold_transfer']
    return redirect('/')

def reset(request):
    request.session.pop('gold_counter')
    request.session.pop('activity_log')
    return redirect('/')
