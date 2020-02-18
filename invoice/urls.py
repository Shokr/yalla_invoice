from django.urls import path

from .views import *

app_name = 'invoice'

urlpatterns = [

    path('', invoices.index, name='index'),

    # INVOICES
    path('invoice/new/', invoices.new_invoice, name='new_invoice'),
    path('invoice/all/', invoices.all_invoices, name='all_invoices'),
    path('invoices/invalid/', invoices.invalid_invoices, name='invalid_invoices'),
    path('invoice/<int:invoice_id>/', invoices.invoice, name='invoice'),
    path('invoice/search/', invoices.search_invoice, name='search_invoice'),
    path('view-invoice/<int:invoice_id>/', invoices.view_invoice, name='view_invoice'),
    path('invoice/<int:invoice_id>/print/', invoices.print_invoice, name='print_invoice'),
    path('invoice/<int:invoice_id>/invalidate/', invoices.invalidate_invoice, name='invalidate_invoice'),

    # ITEMS
    path('invoice/<int:invoice_id>/item/add/', items.add_item, name='add_item'),
    path('invoice/<int:invoice_id>/item/<int:invoiceitem_id>/delete/', items.delete_item, name='delete_item'),

    # CUSTOMERS
    path('customers/', customers.customer_list, name='customer_list'),
    path('customer/<int:customer_id>/', customers.customer, name='customer'),
    path('customer/<int:customer_id>/update/', customers.update_customer, name='update_customer'),
    path('customer/<int:customer_id>/delete/', customers.delete_customer, name='delete_customer'),
    path('customer/new/', customers.new_customer, name='new_customer'),
]
