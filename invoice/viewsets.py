# Third Party imports.
from rest_framework import viewsets, filters

# Local application imports.
from .models import *
from .serializers import *


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'customer__name', 'valid',)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
