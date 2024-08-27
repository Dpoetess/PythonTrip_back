from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    country_id = models.AutoField(primary_key=True),
    iso_code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.iso_code
class Location(models.Model):
    loc_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='locations')
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Attraction(Location):
    attr_id = models.AutoField(primary_key=True)
    attr_name = models.CharField(max_length=200)
    description = models.TextField()
    category_id = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
