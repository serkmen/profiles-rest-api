from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]

        # HTTP function must return a reponse
        # Ressponse in the format of JSON in either list or dictionary format
        return Response({'message': 'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        # Assign request data to serializer class
        serializer = self.serializer_class(data=request.data)

        # Validate a serializer
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            # Return a message + f is for adding variable to string
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            # Default response returns HTTP200
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
    
    # PK is for primary key for update
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    # Partially update
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    # Delete an object
    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method': 'DELETE'})
