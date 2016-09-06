from django import forms
from django.forms import ModelForm
from accounts.models import Sale, Items


class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ('name', 'seller', 'event', 'quantity', 'amount')

class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ('name', 'description', 'presupuesto', 'quantity',)
