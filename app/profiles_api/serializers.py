# Djnago RestFrameowork feature that converts data inputs
# To Python objects and vice versa
# POST - UPDATE functionality requires serializer
# Serializers take care of normalization of input data
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
