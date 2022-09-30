from django import forms
from django.conf import settings
class BuyingForm(forms.Form):
    your_name = forms.CharField(label='Name',max_length=30)
    your_Phone = forms.CharField(label='Phone' ,max_length=15)
    your_Email = forms.EmailField(label='Email',max_length=30)
    your_Card = forms.CharField(label='Card Number',max_length=19)
    your_Date = forms.CharField(label='Expiry Date',max_length=5)
    your_CVV = forms.CharField(label='CVV',max_length=4)