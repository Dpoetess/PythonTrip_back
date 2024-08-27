from django.urls import path, include
from rest_framework import routers
from itineraries import views

router = routers.DefaultRouter()
router.register('itineraries', views.ItineraryView, 'itineraries')

urlpatterns = [
    path('', include(router.urls)),

]
