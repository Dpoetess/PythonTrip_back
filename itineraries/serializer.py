from rest_framework import serializers
from .models import Itinerary


class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        # Automatically assign the user to the itinerary
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)