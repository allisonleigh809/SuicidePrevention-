from django.contrib import admin
from .models import Mood
from .models import Sleep 
# Register your models here.
admin.site.register(Mood)
admin.site.register(Sleep)

