import datetime
from django.db import models
from django.contrib.auth.models import User

class DailyTasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    steps = models.PositiveIntegerField(default=0)
    pushups = models.PositiveSmallIntegerField(default=0)
    situps = models.PositiveSmallIntegerField(default=0)
    squats = models.PositiveSmallIntegerField(default=0)
    planks = models.PositiveSmallIntegerField(default=0)
    sphinxes = models.PositiveSmallIntegerField(default=0)
    workout = models.PositiveSmallIntegerField(default=0)
    