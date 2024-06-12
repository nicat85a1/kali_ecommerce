from django import forms

class OrderForm(forms.Form):
    first_name = forms.CharField(label="first_name:")
    last_name = forms.CharField(label="last_name:")
    phone = forms.CharField(label="phone:")
    address = forms.CharField(label="address:")