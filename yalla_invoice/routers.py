# Third party imports.
from rest_framework import routers

# Local application imports.
from invoice.viewsets import *


router = routers.DefaultRouter()

router.register(r'invoice', InvoiceViewSet)
router.register(r'Customer', CustomerViewSet)
