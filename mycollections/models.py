from django.contrib.auth.models import User
from django.db import models
from countries.models import Location
from itineraries.models import Itinerary


class MyCollection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_collection')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    itin_id = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='itineraries_collection')
    loc_id = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locations_collection')

    def __str__(self):
        return self.collection_id
