"""User model for this project"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model for this project"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
