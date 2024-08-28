from django.db import models
from django.contrib.auth.models import User
from countries.models import Attraction


class Itinerary(models.Model):
    itin_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='itineraries')
    name = models.CharField(max_length=255)
    duration = models.DurationField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_collaborative = models.BooleanField(default=False)
    collaborators = models.ManyToManyField(User, related_name='collaborated_itineraries', blank=True)

    def __str__(self):
        return self.name

class ItineraryDay(models.Model):
    day_id = models.AutoField(primary_key=True)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='days')
    day_number = models.IntegerField()
    day_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Day {self.day_number} - {self.itinerary.name}"

class ItineraryLocation(models.Model):
    itin_loc_id = models.AutoField(primary_key=True)
    day = models.ForeignKey(ItineraryDay, on_delete=models.CASCADE, related_name='itinerary_locations')
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.attraction.attr_name} on {self.day}"
