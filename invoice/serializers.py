# Third party imports.
from rest_framework import serializers

# Local application imports.
from .models import *


class InvoiceSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = Invoice
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = Customer
        fields = '__all__'
