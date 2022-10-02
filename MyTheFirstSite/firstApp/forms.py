from django import forms
from price.models import PriceTable

list_pizz = [obj.pt_title for obj in PriceTable.objects.all()]
choice_pizz = tuple(zip(list_pizz, list_pizz))


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    order = forms.TypedChoiceField(choices=choice_pizz, widget=forms.Select(attrs={'class': 'form-control'}))
