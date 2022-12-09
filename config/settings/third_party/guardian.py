"""
django-guardian
* https://django-filter.readthedocs.io/en/stable/index.html
"""
from ..django import AUTHENTICATION_BACKENDS, INSTALLED_APPS

INSTALLED_APPS.append("guardian")

AUTHENTICATION_BACKENDS.append("guardian.backends.ObjectPermissionBackend")
