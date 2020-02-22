from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(InvoiceItem)


class InvoiceAdmin(admin.ModelAdmin):
    search_fields = ['invoice_code']

    list_display = (
        'invoice_code',
        'date_created',
        'user',
    )

    readonly_fields = (
        'user',
    )


admin.site.register(Invoice, InvoiceAdmin)
