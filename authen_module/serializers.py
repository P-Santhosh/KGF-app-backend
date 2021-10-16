from authen_module.models import Customer
from authen_module.models import Loan
from authen_module.models import User
from rest_framework_mongoengine import serializers as mongoserializers


class CustomerSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class LoanSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class UserSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'
