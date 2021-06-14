from django import forms
from django.forms import ModelForm
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = Product.field_names

    def clean_price(self, *args, **kwargs):
        value = self.cleaned_data.get('price')
        if value > 1000:
            raise ValidationError("Product is too expensive")
        return value

    def clean_description(self, *args, **kwargs):
        value = self.cleaned_data.get('description')
        if len(value) < 20:
            raise ValidationError("Product must have a good description")
        return value
