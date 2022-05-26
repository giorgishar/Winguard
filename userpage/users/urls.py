from django import views
from django.urls import path
from .views import change_password, profile

urlpatterns = [
    path('', profile, name='user_profile'),
    path('password/', change_password, name='change_password')
]
