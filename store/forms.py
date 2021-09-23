from django import forms

from .models import  Product, Order, Jobs

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sortno']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'sortno': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'sortno'
            })
        }

class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['name', 'sortno']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'sortno': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'sortno'
            })
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'company', 'customer', 'phone', 'email', 'product', 'size', 'papergramm', 'price', 'jobs', 'count'
        ]

        widgets = {
            'company': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'company'
            }),
            'customer': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'customer'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'phone'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'email'
            }),
            'product': forms.Select(attrs={
                'class': 'form-control', 'id': 'product'
            }),
            'size': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'size'
            }),
            'papergramm': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'papergramm'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'price'
            }),
            'jobs': forms.Select(attrs={
                'class': 'form-control', 'id': 'jobs'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'price'
            }),
            'count': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'count'
            }),
        }

