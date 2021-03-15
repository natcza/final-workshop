from django import forms
from django.forms import formset_factory

from app1.models import Topping


# django Formset
# class ToppingForm(forms.Form):
#     toppings = Topping.objects.all()
#     i = 1
#     tab = []
#     for topping in toppings:
#         t = (i, topping.name + ", " + str(topping.price) + " zl" + "id=" + str(topping.pk))
#         i += 1
#         tab.append(t)
#     topp = forms.MultipleChoiceField(label="Dodatki", help_text="Mozesz wybrac dwa dodatki!",
#                                      widget=forms.CheckboxSelectMultiple, choices=tab)
#     # topp = forms.ChoiceField(label="Dodatki", widget=forms.RadioSelect, choices=tab, required=True)


# class ToppingForm(forms.Form):
#     topping = forms.ModelMultipleChoiceField(queryset=Topping.objects.all())

# gdy dziedziczymy z modelform (kreowanie automatycznych formularzy dla modeli)
# class Meta:
#     model = Topping
#     fields = ('name',)

class ToppingForm(forms.ModelForm):
    number = forms.IntegerField(min_value=0, required=False)
    name = forms.CharField(disabled=True, required=False)
    price = forms.DecimalField(required=False, disabled=True)

    class Meta:
        model = Topping
        fields = ['name', 'price']
        # widgets = {
        #     'name': Charfield(attrs={'cols': 80, 'rows': 20}),
        # }
