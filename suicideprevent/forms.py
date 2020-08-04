from django import forms
from .models import Mood


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
