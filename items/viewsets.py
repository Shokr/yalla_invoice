# Third Party imports.
from rest_framework import viewsets, filters

from .models import *
from .serializers import *


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'name', 'code',)
