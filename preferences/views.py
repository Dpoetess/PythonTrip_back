from rest_framework import viewsets, permissions
from .models import Category
from .serializer import PreferenceSerializer


class PreferenceViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = PreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]
