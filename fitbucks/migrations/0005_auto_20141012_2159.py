# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitbucks', '0003_auto_20141012_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytasks',
            name='date',
            field=models.DateField(default=b'2014-10-12'),
        ),
    ]
