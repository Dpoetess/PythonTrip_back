from django.db import models
from django.contrib.auth.models import User
#from locations.models import Location

class Itinerary(models.Model):
    itin_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #loc = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    duration = models.DurationField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_collaborative = models.BooleanField(default=False)

    def __str__(self):
        return self.name