from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from itineraries.models import Itinerary
from countries.models import Location


class Preference(models.Model):
    preferences_id = models.AutoField(primary_key=True),
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    itin_id = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='itineraries')
    loc_id = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locations')
    collection_id = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='collections')

    def __str__(self):
        return self.preferences_id


