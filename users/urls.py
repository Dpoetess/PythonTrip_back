from django.urls import include, path
from rest_framework import routers
from .views import RegisterView, UserLoginView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login')
]
