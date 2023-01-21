from django.urls import path
from skill import views

urlpatterns = [
    path('myskills/',views.skill,name="skill"),
]
