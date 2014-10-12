# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitbucks', '0002_auto_20141012_0410'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dailytasks',
            unique_together=set([('user', 'date')]),
        ),
    ]
