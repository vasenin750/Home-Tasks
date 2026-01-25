from django import forms
from products.models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['user', 'product', 'quantity'] # Поля формы должны называться также как поля модели Order
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }