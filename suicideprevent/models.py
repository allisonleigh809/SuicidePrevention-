from django.db import models
from location_field.models.plain import PlainLocationField


# Create your models here.
class Mood(models.Model):
    profile_face = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    
    mood_tracker = models.CharField(max_length=255, null=True, blank=True)
    date_mood = models.DateField(null=True, blank=True)
    
    
    
    sleep_tracker= models.CharField(max_length=255, null=True, blank=True)
    date_sleep = models.DateField(null=True, blank=True)
    
    affirmations = models.CharField(max_length=255, null=True, blank=True)
    
    notification_alerts = models.CharField(max_length=255, null=True, blank=True)
    
    self_care = models.CharField(max_length=255, null=True, blank=True)

    resources = models.CharField(max_length=255, null=True, blank=True)
    
    emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    

    def __str__(self):
         return f"{self.mood_tracker}"
              

    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    
    