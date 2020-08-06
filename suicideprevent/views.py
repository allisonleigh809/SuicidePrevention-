from django.shortcuts import render
from .models import Mood 
from .forms import moodsForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.contrib.auth.models import User

# Create your views here.
def list_moods(request):
  moods = Mood.objects.all()
  return render(request, "moods/list_moods.html",                        {"moods": moods})
  
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
      return render(request, "moods/homepage.html")

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

