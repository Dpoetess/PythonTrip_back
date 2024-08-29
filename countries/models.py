from django.db import models

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='Unnamed Country')
    iso_code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.iso_code
class Location(models.Model):
    loc_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='countries')
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Attraction(models.Model):
    attr_id = models.AutoField(primary_key=True)
    attr_name = models.CharField(max_length=200)
    attr_description = models.TextField(blank=True, null=True)
    attr_category_id = models.IntegerField()
    attr_image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

