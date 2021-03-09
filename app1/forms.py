from django import forms
from app1.models import Topping

#django Formset
class ToppingForm(forms.Form):
    toppings = Topping.objects.all()
    i = 1
    tab = []
    for topping in toppings:
        t = (i, topping.name + ", " + str(topping.price) + " zl" + "id=" + str(topping.pk))
        i += 1
        tab.append(t)
    topp = forms.MultipleChoiceField(label="Dodatki", help_text="Mozesz wybrac dwa dodatki!",
                                     widget=forms.CheckboxSelectMultiple, choices=tab)
    # topp = forms.ChoiceField(label="Dodatki", widget=forms.RadioSelect, choices=tab, required=True)
