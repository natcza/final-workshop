from django import forms
from app1.models import Topping


class ToppingForm(forms.Form):
    toppings = Topping.objects.all()
    i = 1
    tab = []
    for topping in toppings:
        t = (i, topping.name + ", " + str(topping.price) + " zl")
        tab.append(t)
    Dodatki = forms.MultipleChoiceField(help_text="Mozesz wybrac dwa dodatki!", widget=forms.CheckboxSelectMultiple, choices=tab)


