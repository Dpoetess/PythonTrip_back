from rest_framework import viewsets, permissions
from .models import MyCollection
from .serializer import MyCollectionSerializer

class MyCollectionViewSet(viewsets.ModelViewSet):
    queryset = MyCollection.objects.all()
    serializer_class = MyCollectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
