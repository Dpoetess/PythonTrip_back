from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, LocationViewSet, AttractionViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'countries', LocationViewSet)
router.register(r'attractions', AttractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]