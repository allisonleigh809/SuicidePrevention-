from django.db import models
from location_field.models.plain import PlainLocationField


# Create your models here.
class Mood(models.Model):
    profile_face = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    
    mood_tracker = models.CharField(max_length=255, null=True, blank=True)
    date_mood = models.DateField(null=True, blank=True)
    
    
    
    sleep_tracker= models.CharField(max_length=255, null=True, blank=True)
    date_sleep = models.DateField(null=True, blank=True)
    
    affirmations = models.CharField(max_length=255, null=True, blank=True)
    
    notification_alerts = models.CharField(max_length=255, null=True, blank=True)
    
    self_care = models.CharField(max_length=255, null=True, blank=True)

    
    resources = models.CharField(max_length=255, null=True, blank=True)
    
    emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    
    city = models.CharField(max_length=255, default='0000000', editable=False)
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
         return f"{self.mood_tracker}"
              
# class Place(models.Model):
#     city = models.CharField(max_length=255)
#     location = PlainLocationField(based_fields=['city'], zoom=7)

# class ProfileFace(models.Model):    
#     profile_face = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
