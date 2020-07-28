from django import forms
from .models import Mood

class moodsForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = [
            'album_title',
            'artist_name',
            'date_released',    
        ]