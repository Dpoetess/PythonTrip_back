from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from itineraries.models import Itinerary
from countries.models import Location
from mycollections.models import MyCollection


class Preference(models.Model):
    preferences_id = models.AutoField(primary_key=True),
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_preferences', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_preferences', null=True, blank=True)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='itinerary_preferences', null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location_preferences', null=True, blank=True)
    collection = models.ForeignKey(MyCollection, on_delete=models.CASCADE, related_name='collection_preferences', null=True, blank=True)

    class Meta:
        unique_together = ('user', 'location')  # Ensure unique preference per user-location combination

    def __str__(self):
        return f"Preference {self.preferences_id} for user {self.user}"


