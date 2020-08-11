from django.db import models


# Create your models here.
class Mood(models.Model):
  smile_emoji = models.CharField(max_length=255, null=True, blank=True)
  name = models.CharField(max_length=255, null=True, blank=True)
  
  def __str__(self):
    return f"{self.name}"

class MoodTracker(models.Model):
    profile_face = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    mood = models.ForeignKey('Mood', on_delete = models.CASCADE)
    date_added = models.DateField(null=True, blank=True, auto_now_add=True)  

    def __str__(self):
         return f"{self.mood}"

class Sleep(models.Model):
  smile_emoji = models.CharField(max_length=255, null=True, blank=True)
  name = models.CharField(max_length=255, null=True, blank=True)
  
  def __str__(self):
    return f"{self.smile_emoji}"

class SleepTracker(models.Model):
    profile_face = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    sleep = models.ForeignKey('Sleep', on_delete = models.CASCADE)
    date_added = models.DateField(null=True, blank=True, auto_now_add=True)  

    def __str__(self):
         return f"{self.sleep}"
              

              
# class Place(models.Model):
#     city = models.CharField(max_length=255)
#     location = PlainLocationField(based_fields=['city'], zoom=7)

# class ProfileFace(models.Model):    
#     profile_face = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
