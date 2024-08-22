from rest_framework import serializers
from users.models import User
# Serializamos la data que trae ese objeto, en este caso el objeto User
class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = '__all__'