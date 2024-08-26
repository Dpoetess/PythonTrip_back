from django.urls import path, include
from rest_framework import routers
from .views import ItineraryView, ItineraryListView, ItineraryCreateView, ItineraryUpdateView, ItineraryDeleteView

router = routers.DefaultRouter()
router.register('itinerary', ItineraryView, 'itinerary')

urlpatterns = [
    path('', include(router.urls)),
    path('itinerary/', ItineraryView.as_view(), name='itinerary'),
    path('', ItineraryListView.as_view(), name='itinerary-list'),
    path('itinerary_add/', ItineraryCreateView.as_view(), name='itinerary-add'),
    path('itinerary_edit/', ItineraryUpdateView.as_view(), name='itinerary-edit'),
    path('itinerary_delete/', ItineraryDeleteView.as_view(), name='itinerary-delete'),
]