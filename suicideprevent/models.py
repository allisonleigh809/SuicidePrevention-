from django.db import models

# Create your models here.
class Mood(models.Model):
    happy_face = models.CharField(max_length=255, null=True, blank=True)
    sad_face= models.CharField(max_length=255, null=True, blank=True)
    angry_face = models.CharField(max_length=255, null=True, blank=True)
    cry_face = models.CharField(max_length=255, null=True, blank=True)
    neutral_face = models.CharField(max_length=255, null=True, blank=True)
    annoyed_face = models.CharField(max_length=255, null=True, blank=True)
    disgust_face = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
         return f"{self.neutral_face}"
         
        