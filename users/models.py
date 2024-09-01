from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=80, null=False)
    last_name = models.CharField(max_length=80, null=False)
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=9, null=False)
    preferences = models.JSONField(default=dict, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_name})"