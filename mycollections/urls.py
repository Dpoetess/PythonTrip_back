from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyCollectionViewSet

router = DefaultRouter()
router.register(r'mycollections', MyCollectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]