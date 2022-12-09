"""
The serializer of Permission
"""
from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    """
    The serializer of Permission
    """

    class Meta:
        model = Permission
        fields = "__all__"
