"""
URL Dispatcher
* https://docs.djangoproject.com/en/4.1/topics/http/urls/

Router
* https://www.django-rest-framework.org/api-guide/routers/
"""
from rest_framework import routers

from .viewsets import ContentTypeViewSet, GroupViewSet, PermissionViewSet, UserViewSet

router = routers.DefaultRouter()
router.register("contenttypes", ContentTypeViewSet)
router.register("groups", GroupViewSet)
router.register("permissions", PermissionViewSet)
router.register("users", UserViewSet)
