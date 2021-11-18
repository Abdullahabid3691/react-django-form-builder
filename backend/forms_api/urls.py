from django.urls import path, include
from rest_framework import routers

from .viewsets import FormBuilderViewSet

router = routers.DefaultRouter()
router.register('form_builder', FormBuilderViewSet, 'form_builder_api')

urlpatterns = [
    path('', include(router.urls)),
]
