# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitbucks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailytasks',
            name='date',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='planks',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='pushups',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='situps',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='sphinxes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='squats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='steps',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dailytasks',
            name='workout',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
