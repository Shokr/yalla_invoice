# Third party imports.
from rest_framework import serializers

# Local application imports.
from .models import *


class ItemSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = Item
        fields = '__all__'
