"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from suicideprevent import views as suicideprevent_views


urlpatterns = [

    path('login/', LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="registration/login.html"), name='logout'),
    
    path('admin/', admin.site.urls),
    
    path('', suicideprevent_views.homepage,
    name='homepage'),
    
    path('moods/mood_tracker', suicideprevent_views.mood_tracker, name='tracker'),

    path('moods/add', suicideprevent_views.add_moods, name='add_moods'),
    
    path('moods/<int:pk>/delete/', suicideprevent_views.delete_moods, name='delete_moods'),
    
    path('moods/<int:pk>/edit/',suicideprevent_views.edit_moods, name='edit_moods'),

    path('moods/list_mood_trackers/',suicideprevent_views.list_mood_trackers, name='list_mood_tracker'),

    path('moods/self_care/',suicideprevent_views.self_care, name='self_care'),
    # put in profile and mood tracker in url
   path('moods/resources/',suicideprevent_views.resources, name='resources'),

   path('moods/calendar/',suicideprevent_views.calendar, name='calendar'),
    

    
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


# add to url into views when created line 25-26
# path('', suicideprevent_views.mood_tracker,
#       name='mood_tracker'), 