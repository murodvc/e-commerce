from django import forms
from app.models import  Customers


class CustomersModelForm(forms.ModelForm):
    class Meta:
        model = Customers
        # fields = ['name', 'description', 'price', 'image', 'rating', 'discount']
        exclude = ()
