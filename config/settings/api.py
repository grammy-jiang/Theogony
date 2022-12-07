"""
Django settings for the application of api.
"""
from .django import INSTALLED_APPS

INSTALLED_APPS.append("api")

AUTH_USER_MODEL = "api.User"
