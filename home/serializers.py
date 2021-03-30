#models fields selected for the use in api | serializer - A model for API
from rest_framework import serializers, viewsets
from .models import *

# Serializers define the API representation.
class ItemSerializer(serializers.ModelSerializer):
    class Meta:      #class inside class = meta class
        model = Item
        fields = ['title', 'item_code', 'price', 'category','description', 'discounted_price', 'label', 'image']

class CartSerializer(serializers.ModelSerializer):
    class Meta:      #class inside class = meta class
        model = OrderItem
        fields = "__all__"