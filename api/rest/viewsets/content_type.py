"""
The viewset of ContentType
"""
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from ..serializers import ContentTypeSerializer


class ContentTypeViewSet(viewsets.ModelViewSet):
    """
    The viewset of ContentType
    """

    permission_classes = (IsAdminUser,)

    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
