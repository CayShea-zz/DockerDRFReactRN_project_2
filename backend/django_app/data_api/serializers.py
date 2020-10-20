from rest_framework import serializers
from data_api.models import ThingaRoo

class ThingarooSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)

    class Meta:
        model = ThingaRoo
        fields = '__all__'