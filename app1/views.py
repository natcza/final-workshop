from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from app1.models import (
    Pizza,
    Topping, Order,
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

        ctx = {
            'pizza': pizza,
            'toppings': toppings,
            'message': message,
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        form = ToppingForm(request.POST)
        if not form.is_valid():  # TODO if not_valid():
            return redirect('pizza-list')
        pizza_id = kwargs['pk']
        chosen_pizza = get_object_or_404(Pizza, pk=pizza_id)
        #TODO skorzystac z metody sum musimy miec cene skladnikow plus cena pizzy
        topp = form.cleaned_data.get('topp')
        order = Order.objects.create(order_price=, note)
        ordered_pizza = Pizza.objects.create(name=chosen_pizza.name, size=chosen_pizza.size, price=chosen_pizza.price)
        for i in topp:
            ordered_pizza.toppings.add(Topping.objects.get(pk=int(i)))
        return redirect('pizza-list')


