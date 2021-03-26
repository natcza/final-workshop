from django import forms
from django.forms import formset_factory

from app1.models import Topping


class ToppingForm(forms.ModelForm):
    number = forms.IntegerField(min_value=0, required=False)
    name = forms.CharField(disabled=True, required=False)
    price = forms.DecimalField(required=False, disabled=True)

    class Meta:
        model = Topping
        fields = ['name', 'price']
