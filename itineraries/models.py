from django.db import models
from django.contrib.auth.models import User

class Itinerary(models.Model):
    itin_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    duration = models.DurationField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_collaborative = models.BooleanField(default=False)
    collaborators = models.ManyToManyField(User, related_name='collaborated_itineraries', blank=True)

    def __str__(self):
        return self.name
