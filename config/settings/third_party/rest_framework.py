"""
Django REST framework
* https://www.django-rest-framework.org/
"""
from ..django import INSTALLED_APPS

INSTALLED_APPS.extend(
    (
        "rest_framework",
        "rest_framework_json_api",
    )
)
