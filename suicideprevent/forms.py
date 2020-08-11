from django import forms
from .models import MoodTracker
from .models import SleepTracker

class moodsForm(forms.ModelForm):
    class Meta:
        model = MoodTracker
        fields = [
          'mood',
          
        ]

class sleepsForm(forms.ModelForm):
    class Meta:
        model = SleepTracker
        fields = [
          'sleep',
          
        ]


