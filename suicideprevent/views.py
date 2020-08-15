from django.shortcuts import render
from .models import Mood 
from .models import Sleep
from .forms import moodsForm
from .forms import sleepsForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.contrib.auth.models import User
from .models import MoodTracker


# Create your views here.
def list_mood_trackers(request):
    moods_trackers = MoodTracker.objects.filter(user=request.user)
    return render(request, "moods/list_mood_trackers.html", {"moods_trackers": moods_trackers})
  
def add_moods(request):
    if request.method == 'GET':
        form = moodsForm()
    else:
        form = moodsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_moods')

    return render(request, "moods/add_moods.html", {"form": form})  

def delete_moods(request, pk):
    mood = get_object_or_404(Mood, pk=pk)
    if request.method == 'POST':
        mood.delete()
        return redirect(to='list_moods')

    return render(request, "moods/delete_moods.html",
                  {"mood": mood})

def edit_moods(request, pk):
    mood = get_object_or_404(Mood, pk=pk)
    if request.method == 'GET':
        form = moodsForm(instance=mood)
    else:
        form = moodsForm(data=request.POST, instance=mood)
        if form.is_valid():
            form.save()
            return redirect(to='list_moods')

    return render(request, "moods/edit_moods.html", {
        "form": form,
        "mood": mood
    })


def homepage(request):
    moods = Mood.objects.all()
    sleeps = Sleep.objects.all()
    return render(request, "moods/homepage.html", 
    {"moods": moods, "sleeps": sleeps}) 

def mood_tracker(request, pk):
    mood = get_object_or_404(Mood, pk=pk)
    mood_tracker = MoodTracker.objects.create(user=request.user, mood=mood)
    return redirect(to="progress_bar")

def self_care(request):
      return render(request, "moods/self_care.html")

def resources(request):
      return render(request, "moods/resources.html")

def health(request):
      return render(request, "moods/health.html")

def opportunites(request):
      return render(request, "moods/opportunites.html")

def adventures(request):
      return render(request, "moods/adventures.html")


def progress_bar(request):
      return render(request, "moods/progress_bar.html")

def progress_bar2(request):

      return render(request, "moods/progress_bar2.html")

def index(request):

      return render(request, "moods/index.html")

def submit_button(request):

      return render(request, "moods/submit_button.html")



