"""
The serializer of User
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    The serializer of User
    """

    class Meta:
        model = User
        fields = "__all__"
