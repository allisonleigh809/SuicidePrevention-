from django import forms
from .models import Mood
from .models import Place

class moodsForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = [
            'mood_tracker',
            'sleep_tracker',
            'notification_alerts',
            'emergency_contact',
            'resources',    
        ]

class placesForm(forms.ModelForm):
  class Meta:
        model = Place
        fields = [
            'city',
            'location',
              
        ]
  