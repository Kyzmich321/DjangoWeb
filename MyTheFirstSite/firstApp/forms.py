from django import forms
from django.core import validators
from django.forms import ModelForm
from price.models import PriceTable
from .models import Order

list_pizz = [obj.pt_title for obj in PriceTable.objects.all()]
choice_pizz = tuple(zip(list_pizz, list_pizz))


class OrderForm(ModelForm):
    # name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}),
    #                         validators=[validators.RegexValidator(regex='\d{10}')],
    #                         error_messages={'invalid': 'The number must have 10 digits. For example, 0678812345'}
    #                         )
    order = forms.TypedChoiceField(choices=choice_pizz, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = ('order_name', 'order_phone')
        widgets = {'order_name': forms.TextInput(attrs={'class': 'form-control',}),
                   'order_phone': forms.TextInput(attrs={'class': 'form-control'})}
        help_texts={'order_name': 'Please write you name.',
                    'order_phone': 'Please write you phone.'}



