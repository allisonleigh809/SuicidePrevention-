from django.shortcuts import render
from .models import Mood 
from .forms import moodsForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.contrib.auth.models import User

# Create your views here.
def list_contacts(request):
  moods = Mood.objects.all()
  return render(request, "mood/list_contacts.html",                        {"moods": moods})
  
def add_contacts(request):
    if request.method == 'GET':
        form = moodsForm()
    else:
        form = moodsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "mood/add_contacts.html", {"form": form})  

def delete_moods(request, pk):
    mood = get_object_or_404(Mood, pk=pk)
    if request.method == 'POST':
        mood.delete()
        return redirect(to='list_contacts')

    return render(request, "mood/delete_contacts.html",
                  {"mood": mood})

def edit_contacts(request, pk):
    mood = get_object_or_404(Mood, pk=pk)
    if request.method == 'GET':
        form = moodsForm(instance=mood)
    else:
        form = moodsForm(data=request.POST, instance=mood)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "mood/edit_contacts.html", {
        "form": form,
        "mood": mood
    })
