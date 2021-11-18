from rest_framework import serializers

from form_builder.models import Form as FromBuilder


class FormBuilderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FromBuilder
        fields = '__all__'
