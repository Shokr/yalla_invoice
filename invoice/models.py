from django.db import models
from items.models import Item

import uuid


class Customer(models.Model):
    """
       Models for a customer.
    """
    name = models.CharField(max_length=256, null=False, blank=False, help_text='Enter Customer or Company')
    address = models.CharField(max_length=100, null=True, blank=True, help_text='Enter address of customer or Company')
    city = models.CharField(max_length=100, null=True, blank=True, help_text='Enter the city of the address')
    region = models.CharField(max_length=50, null=True, blank=True, help_text='Enter the region of the address')
    country = models.CharField(max_length=100, null=True, blank=True, help_text='Enter the country of the address')
    email = models.EmailField(null=True, blank=True, help_text='Enter the email of the customer or Company')

    def __str__(self):
        """
           Displays a human-readable representation of Customer Model
        """
        return self.name

    def invoices(self):
        """
           Returns all the invoices of a customer.
        """
        return Invoice.objects.filter(customer=self).count()


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_code = models.UUIDField(default=uuid.uuid4, editable=False)
    valid = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def total_items(self):
        total = 0
        items = self.invoiceitem_set.all()

        for item in items:
            total += item.item.cost * item.qty

        return total

    def total(self):
        items = self.total_items()
        return items


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return self.item

    def total(self):
        return self.item.cost * self.qty

# class InvoiceItem(models.Model):
#     invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
#     name = models.CharField(max_length=128)
#     description = models.TextField()
#     cost = models.DecimalField(decimal_places=2, max_digits=10)
#     qty = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
#     def total(self):
#         return self.cost * self.qty
