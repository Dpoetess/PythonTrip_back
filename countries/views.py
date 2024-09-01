from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Country, Location, Attraction
from .serializer import CountrySerializer, LocationSerializer, AttractionSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        loc_id = self.request.query_params.get('loc_id')
        try:
            loc_id = int(loc_id) if loc_id is not None else None
        except ValueError:
            loc_id = None

        if loc_id is not None:
            return self.queryset.filter(location__loc_id=loc_id)
        return self.queryset