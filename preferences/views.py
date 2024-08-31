from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from countries.models import Location
from .models import Category, Preference
from .serializer import PreferenceSerializer


class PreferenceViewSet(viewsets.ModelViewSet):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        location_id = request.data.get('location')
        if not location_id:
            return Response({"error": "Location ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        location = Location.objects.filter(id=location_id).first()
        if not location:
            return Response({"error": "Location not found."}, status=status.HTTP_404_NOT_FOUND)

        # Ensure the user doesn't already have this location saved
        if Preference.objects.filter(user=request.user, location=location).exists():
            return Response({"message": "Location already saved."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new preference entry for the saved location
        preference = Preference.objects.create(user=request.user, location=location)
        serializer = self.get_serializer(preference)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        location_id = request.data.get('location')
        if not location_id:
            return Response({"error": "Location ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        location = Location.objects.filter(id=location_id).first()
        if not location:
            return Response({"error": "Location not found."}, status=status.HTTP_404_NOT_FOUND)

        # Remove the location from user's preferences
        preference = Preference.objects.filter(user=request.user, location=location).first()
        if not preference:
            return Response({"error": "Location not found in preferences."}, status=status.HTTP_404_NOT_FOUND)

        preference.delete()
        return Response({"message": "Location removed from preferences."}, status=status.HTTP_204_NO_CONTENT)
