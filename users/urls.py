from django.urls import include, path
from rest_framework import routers
from .views import RegisterView, UserLoginView, UserDetailView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user/', UserDetailView.as_view(), name='user_detail')
]
