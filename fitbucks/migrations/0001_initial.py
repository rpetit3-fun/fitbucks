# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('steps', models.PositiveIntegerField(default=0, blank=True)),
                ('pushups', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('situps', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('squats', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('planks', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('sphinxes', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('workout', models.PositiveSmallIntegerField(default=0, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
