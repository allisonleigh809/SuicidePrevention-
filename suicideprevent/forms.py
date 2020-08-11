from django import forms
from .models import MoodTracker


class moodsForm(forms.ModelForm):
    class Meta:
        model = MoodTracker
        fields = [
          'mood',
        ]


