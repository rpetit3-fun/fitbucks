from django.db import models
from django.contrib.auth.models import User

class DailyTasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    steps = models.PositiveIntegerField(default=0, blank=True)
    pushups = models.PositiveSmallIntegerField(default=0, blank=True)
    situps = models.PositiveSmallIntegerField(default=0, blank=True)
    squats = models.PositiveSmallIntegerField(default=0, blank=True)
    planks = models.PositiveSmallIntegerField(default=0, blank=True)
    sphinxes = models.PositiveSmallIntegerField(default=0, blank=True)
    workout = models.PositiveSmallIntegerField(default=0, blank=True)
    