"""
The serializer of Group
"""
from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    The serializer of Group
    """

    class Meta:
        model = Group
        fields = "__all__"
