from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'fitbucks.views.index', name='home'),
    url(r'^daily-tasks/', 'fitbucks.views.daily_tasks', name='daily_tasks'),
    url(r'^missions/', 'fitbucks.views.missions', name='missions'),
    url(r'^quests/', 'fitbucks.views.quests', name='quests'),
    url(r'^rewards/', 'fitbucks.views.rewards', name='rewards'),
    
)
