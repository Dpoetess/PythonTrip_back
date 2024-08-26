from django.urls import include, path
from rest_framework import routers
from .views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register')
]
