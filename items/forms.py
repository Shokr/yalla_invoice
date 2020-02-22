from __future__ import unicode_literals

from django import forms
from items.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
