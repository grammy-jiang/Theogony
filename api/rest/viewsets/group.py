"""
The viewset of Group
"""
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from ..serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    The viewset of Group
    """

    permission_classes = (IsAdminUser,)

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
