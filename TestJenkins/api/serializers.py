from rest_framework import serializers

from api.models import CarModel

class CarSerializer(serializers.ModelSerializer):
     class Meta:
        model = CarModel
        fields = ('mark', 'name', 'engine', 'cylyner_count', 'oil_type')
