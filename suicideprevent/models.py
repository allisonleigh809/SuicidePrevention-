from django.db import models

# Create your models here.
class Mood(models.Model):
    mood_tracker = models.CharField(max_length=255, null=True, blank=True)
    date_mood = models.DateField(null=True, blank=True)
    sleep_tracker= models.CharField(max_length=255, null=True, blank=True)
    date_sleep = models.DateField(null=True, blank=True)
    ways_help = models.CharField(max_length=255, null=True, blank=True)
    notification_alerts = models.CharField(max_length=255, null=True, blank=True)
    self_care = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    profile_face = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    resources = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
         return f"{self.mood_tracker}"
              
# Create your models here.
