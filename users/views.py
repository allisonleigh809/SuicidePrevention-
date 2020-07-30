from django.shortcuts import render
from .models import User
from .models import Moods

# Create your views here.
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'May our words lift you always...'
    user.save()

# Create your views here.
