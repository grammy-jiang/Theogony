"""
Django REST framework
* https://www.django-rest-framework.org/

Django REST framework JSON:API
* https://django-rest-framework-json-api.readthedocs.io/en/stable/index.html
"""
from ..django import INSTALLED_APPS

INSTALLED_APPS.extend(
    (
        "rest_framework",
        "rest_framework_json_api",
    )
)
