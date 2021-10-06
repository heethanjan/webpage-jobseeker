from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """serialiize a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
        'password': {
        'write_only':True,
        'style': {'input_type': 'password'}
        }
        }

    def create(self, Validated_data):
        """Create and return  a new user"""
        user = models.UserProfile.objects.create_user(
        email= Validated_data['email'],
        name =  Validated_data['name'],
        password= Validated_data['password']
        )

        return user
