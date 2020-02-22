# Third party imports.
from rest_framework import routers

# Local application imports.
from invoice.viewsets import *
from items.viewsets import ItemViewSet

router = routers.DefaultRouter()

router.register(r'invoice', InvoiceViewSet)
router.register(r'Customer', CustomerViewSet)
router.register(r'Item', InvoiceViewSet)
