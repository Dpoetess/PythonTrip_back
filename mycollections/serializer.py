from rest_framework import serializers
from .models import MyCollection


class MyCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCollection
        fields = '__all__'