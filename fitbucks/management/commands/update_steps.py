'''

'''
import pytz
import subprocess
from optparse import make_option
from datetime import date, datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from fitbucks.models import DailyTasks

class Command(BaseCommand):
    help = 'Insert steps from yesterday into database.'
    option_list = BaseCommand.option_list + (
        make_option('--name', dest='name',
                    help='Name to look up steps for.'),
        make_option('--username', dest='username',
                    help='User ID to store the results under.'),
    )

        
    def handle(self, *args, **options):
        # Required Parameters
        if not options['name']:
            raise CommandError('--name')
        elif not options['username']:
            raise CommandError('--username')
            
        # Get steps
        yesterday = datetime.now(pytz.timezone('US/Eastern')) - timedelta(1)
        yesterday = datetime.strftime(yesterday, "%Y-%m-%d")

        cmd = ['python', '/home/rpetit/repos/fitbit-steps/fitbit-steps.py', 
               '--name', options['name'], '--date', yesterday]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        steps, error = p.communicate()

        user = User.objects.get(username=options['username'])
        try:
            dailytasks = DailyTasks.objects.get(user=user, 
                                                date=yesterday)
            dailytasks.steps = int(steps)
            dailytasks.save()
        except DailyTasks.DoesNotExist:
            dailytasks = DailyTasks.objects.create(user=user, date=yesterday, 
                                                   steps=int(steps))
            dailytasks.save()                                       
