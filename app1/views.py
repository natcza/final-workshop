from django.shortcuts import render
from django.views import View
from app1.models import (
    Pizza,
    Topping,
)

from app1.forms import (
    ToppingForm,
)


class PizzaView(View):
    template_name = 'app1/pizza_view.html'

    def get(self, request, *args, **kwargs):
        pizzas = Pizza.objects.all()
        ctx = {
            'pizzas': pizzas,
        }
        return render(request, self.template_name, ctx)


class PizzaDetailsView(View):
    template_name = 'app1/pizza_details_view.html'

    def get(self, request, *args, **kwargs):
        form = ToppingForm()
        message = None
        pizza_id = kwargs['pk']
        pizza = Pizza.objects.get(pk=pizza_id)
        toppings = Topping.objects.all()
        # i = 1
        # tab = []
        # for topping in toppings:
        #     t = (i, topping.name, topping.price)
        #     tab.append(t)

        ctx = {
            'pizza': pizza,
            'toppings': toppings,
            'message': message,
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = ToppingForm(request.POST)
        breakpoint()
        # if form.is_valid():
