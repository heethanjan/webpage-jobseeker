from rest_framework.views import APIView
from rest_framework.response import Response

class helloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditonal Django view',
        'gives you the most control over you application logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview':an_apiview})
