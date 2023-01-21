from django.urls import path
from service import views

urlpatterns = [
    path('myservice/',views.service,name="service"),
]
