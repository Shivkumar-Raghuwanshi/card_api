from rest_framework import serializers
from .models import Card, Delivered, Pickup, Returned, DeliveryException


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class DeliveredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivered
        fields = '__all__'

class DeliveryExceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryException
        fields = '__all__'

class PickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pickup
        fields = '__all__'

class ReturnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Returned
        fields = '__all__'