from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'location', 'phone_number', 'food_item']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Location'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'food_item': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Your Food'}),
        }