from django.contrib import admin

from django.contrib import admin
from .models import Itinerary, ItineraryDay, ItineraryLocation

admin.site.register(Itinerary)
admin.site.register(ItineraryDay)
admin.site.register(ItineraryLocation)
