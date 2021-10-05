from authen_module.models import Customer
from rest_framework_mongoengine import serializers as mongoserializers


class CustomerSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model=Customer
        fields='__all__'