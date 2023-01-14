from rest_framework import serializers
from .models import Product # Can use .filename if you are importing from the same parent file our car model and serializer file are both in Cars folder

class ProductSerializer(serializers.ModelSerializer): # Set class to app name + serializer
    class Meta: # Where we define small bits of information about serializer class
        model = Product #what model this serializer should be bound to (in this case the Car model)
        fields = ['id', 'title', 'description', 'price', 'inventory_quantity'] # What column are in the model what you can see