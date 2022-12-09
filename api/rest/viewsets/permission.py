"""
The viewset of Permission
"""
from django.contrib.auth.models import Permission
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from ..serializers import PermissionSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """
    The viewset of Permission
    """

    permission_classes = (IsAdminUser,)

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
