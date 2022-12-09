"""
The viewset of User
"""
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from ..serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    The viewset of User
    """

    permission_classes = (IsAdminUser,)

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
