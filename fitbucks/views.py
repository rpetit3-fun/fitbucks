from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html', {}, RequestContext(request))
    
def daily_tasks(request):
    return render_to_response('daily_tasks.html', {}, RequestContext(request))
    
def missions(request):
    return render_to_response('missions.html', {}, RequestContext(request))
    
def quests(request):
    return render_to_response('quests.html', {}, RequestContext(request))
    
def rewards(request):
    return render_to_response('rewards.html', {}, RequestContext(request))

 
