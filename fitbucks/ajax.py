import json
from datetime import datetime

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from fitbucks.models import DailyTasks

@csrf_exempt
def get_daily_stats(request):
    if request.POST and request.is_ajax():
        dailytasks= None
        data = None
        try:
            dailytasks = DailyTasks.objects.get(user=request.user, 
                                                date=request.POST['date'])
        except DailyTasks.DoesNotExist:
            dailytasks = DailyTasks.objects.create(
                user=request.user,
                date=datetime.strptime(request.POST['date'], "%Y-%m-%d")
            )
        data = serializers.serialize('json', [dailytasks])
        return HttpResponse(json.dumps(data), "application/json")
    return HttpResponseRedirect('/daily-tasks/')

