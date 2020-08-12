from django.contrib import admin
from .models import Mood, MoodTracker
from .models import Sleep, SleepTracker
# Register your models here.
admin.site.register(Mood)
admin.site.register(Sleep)
admin.site.register(MoodTracker)
admin.site.register(SleepTracker)

class MoodTrackerAdmin(admin.ModelAdmin):
    fields = ("mood", "user", "date_added")