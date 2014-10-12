from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from fitbucks.forms import DailyTasksForm

def index(request):
    return render_to_response('index.html', {}, RequestContext(request))
    
def daily_tasks(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DailyTasksForm(request.user.id, request.POST)
            if form.is_valid():
                save_results = form.save(request.user.id, request.POST)
                return HttpResponseRedirect('/daily-tasks/')
        else:
            form = DailyTasksForm(request.user.id)
            return render_to_response('daily_tasks.html', {'form':form}, RequestContext(request))
    else:
        return HttpResponseRedirect('/')
    
def missions(request):
    return render_to_response('missions.html', {}, RequestContext(request))
    
def quests(request):
    return render_to_response('quests.html', {}, RequestContext(request))
    
def rewards(request):
    return render_to_response('rewards.html', {}, RequestContext(request))

 
