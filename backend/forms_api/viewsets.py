from rest_framework import viewsets, permissions

from .serializers import FormBuilderSerializer
from form_builder.models import Form as FormBuilder


class FormBuilderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Form to be viewed or edited.
    """
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = FormBuilder.objects.all()
    serializer_class = FormBuilderSerializer
