from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64)

    class Meta:
        model = Trip
        fields = '__all__'
