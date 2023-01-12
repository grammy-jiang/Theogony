"""
django-polymorphic
* https://django-polymorphic.readthedocs.io/en/stable/index.html
"""
from ..django import INSTALLED_APPS

INSTALLED_APPS.insert(
    INSTALLED_APPS.index("django.contrib.contenttypes"), "polymorphic"
)
