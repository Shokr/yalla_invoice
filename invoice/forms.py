from __future__ import unicode_literals

from django import forms
from django.forms import formset_factory
from .models import *


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    """
        Forms for creating a new customer.
    """

    class Meta:
        model = Customer
        fields = ['name', 'address', 'city', 'region', 'country', 'email', ]
        widgets = {'name': forms.TextInput(attrs={"class": "form-control"}),
                   'address': forms.TextInput(attrs={"class": "form-control"}),
                   'city': forms.TextInput(attrs={"class": "form-control"}),
                   'region': forms.TextInput(attrs={"class": "form-control"}),
                   'country': forms.TextInput(attrs={"class": "form-control"}),
                   'email': forms.TextInput(attrs={"class": "form-control"}),
                   }


# class ItemForms(forms.Form):
#     item = forms.CharField(min_length=2, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     cost = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': '0.00', 'class': 'form-control'}))
#     qty = forms.IntegerField(min_value=1)

class ItemForms(forms.Form):
    item = forms.ModelChoiceField(queryset=Item.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    qty = forms.IntegerField(min_value=1)


ItemFormset = formset_factory(ItemForms)
