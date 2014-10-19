from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from registration.forms import RegistrationFormUniqueEmail

from fitbucks.models import DailyTasks

class RegistrationFormWithName(RegistrationFormUniqueEmail):
    first_name = forms.CharField(max_length=50, label='First Name')    
    last_name = forms.CharField(max_length=50, label='Last Name')
    
class DailyTasksForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DailyTasksForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Save'))
        css = 'col-sm-6'
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_id = 'save-daily-task'
        self.helper.form_class = 'input-lg'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Div(
                'workout', 'planks', 'sphinxes',

                css_class=css
            ),
            Div(
                'pushups', 'situps', 'squats',
                Submit('submit', 'Save', css_class='btn-lg'),
                HTML('''
                    <button id="update_steps" type="button" class="btn btn-primary btn-lg">
                        Sync Steps
                    </button>
                '''),
                css_class=css
            ),
            Field('date', type='hidden'),
        )
        
    def save(self, user, POST):
        try:
            # Exists so lets update
            dailytasks = DailyTasks.objects.get(user=user, date=POST['date'])
            dailytasks.workout = POST['workout']
            dailytasks.planks = POST['planks']
            dailytasks.sphinxes = POST['sphinxes']
            dailytasks.pushups = POST['pushups']
            dailytasks.situps = POST['situps']
            dailytasks.squats = POST['squats']
            return dailytasks.save()
        except DailyTasks.DoesNotExists:
            # Does not exist so lets create
            dailytasks = DailyTasks(user=user, **POST)
            return dailytasks.save()

    class Meta:
        model = DailyTasks
        fields = ['workout', 'planks', 'sphinxes',
                  'pushups', 'situps', 'squats', 'date']
        labels = {
            'workout':_('Workout (Minutes)'), 
            'planks':_('Planks (Seconds)'), 
            'sphinxes':_('Sphinxes (Seconds)'),
            'pushups':_('Push Ups'), 
            'situps':_('Sit Ups'), 
            'squats':_('Squats'),
        }
