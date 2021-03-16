from django.forms import modelform_factory, modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from faker.generator import random

from app1.models import (
    Pizza,
    Topping, Order, PizzaOrder, PizzaOrderTops,
)

from app1.forms import (
    ToppingForm,
)


class MainView(View):
    template_name = 'app1/main_view.html'

    def get(self, request):
        pizza = list(Pizza.objects.all().values("name", "price", "description"))
        random.shuffle(pizza)
        return render(request, self.template_name, context={"pizza": pizza})


# class PizzaView(View):
#     template_name = 'app1/pizza_view.html'
#
#     def get(self, request, *args, **kwargs):
#         pizzas = Pizza.objects.all()
#         ctx = {
#             'pizzas': pizzas,
#         }
#         return render(request, self.template_name, ctx)


# class PizzaDetailsView(View):
#     template_name = 'app1/pizza_topping_view.html'
#
#     def get(self, request, *args, **kwargs):
#         form = ToppingForm()
#         message = None
#         pizza_id = kwargs['pk']
#         pizza = Pizza.objects.get(pk=pizza_id)
#         toppings = Topping.objects.all()
#
#         ctx = {
#             'pizza': pizza,
#             'toppings': toppings,
#             'message': message,
#             'form': form,
#         }
#         return render(request, self.template_name, ctx)
#
#     def post(self, request, *args, **kwargs):
# form = ToppingForm(request.POST)
# if not form.is_valid():  # TODO if not_valid():
#     return redirect('pizza-list')
# pizza_id = kwargs['pk']
# chosen_pizza = get_object_or_404(Pizza, pk=pizza_id)
# #TODO skorzystac z metody sum musimy miec cene skladnikow plus cena pizzy
# topp = form.cleaned_data.get('topp')
# # order = Order.objects.create(order_price=, note)
# ordered_pizza = Pizza.objects.create(name=chosen_pizza.name, size=chosen_pizza.size, price=chosen_pizza.price)
# for i in topp:
#     ordered_pizza.toppings.add(Topping.objects.get(pk=int(i)))
# return redirect('pizza-list')


# class PizzaDetailsView(View):
#     template_name = 'app1/pizza_topping_view.html'
#
#     def get(self, request, *args, **kwargs):
#         form = ToppingForm()
#         ToppingFormSet = modelformset_factory(Topping, ToppingForm)
#         formset = ToppingFormSet(queryset=Topping.objects.all())
#         message = None
#         pizza_id = kwargs['pk']
#         pizza = Pizza.objects.get(pk=pizza_id)
#         toppings = Topping.objects.all()
#         context = {
#             'form': form,
#             'pizza': pizza,
#             'formset': formset,
#         }
#         return render(request, self.template_name, context)

# def post(self, request, *args, **kwargs):
#     form = ToppingForm(request.POST)
#     if form.is_valid():


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
        pizza_id = kwargs['pk']
        pizza = get_object_or_404(Pizza, pk=pizza_id)

        ctx = {
            'pizza': pizza,
        }
        return render(request, self.template_name, ctx)


class ToppingView(View):
    template_name = 'app1/topping_view.html'

    def get(self, request, *args, **kwargs):
        toppings = Topping.objects.all()
        ctx = {
            'toppings': toppings,
        }
        return render(request, self.template_name, ctx)


class PizzaToppingsView(View):
    template_name = 'app1/pizza_topping_view.html'

    def get(self, request, *args, **kwargs):
        form = ToppingForm()
        ToppingFormSet = modelformset_factory(Topping, ToppingForm, extra=0)
        formset = ToppingFormSet(queryset=Topping.objects.all())
        message = None
        pizza_id = kwargs['pk']
        pizza = get_object_or_404(Pizza, pk=pizza_id)
        toppings = Topping.objects.all()
        context = {
            'form': form,
            'pizza': pizza,
            'formset': formset,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ToppingForm(request.POST)
        pizza_id = kwargs['pk']
        pizza = get_object_or_404(Pizza, pk=pizza_id)
        ToppingFormSet = modelformset_factory(Topping, ToppingForm, extra=0)
        # formset = ToppingFormSet(queryset=Topping.objects.all())
        formset = ToppingFormSet(request.POST, queryset=Topping.objects.all())
        user = request.user
        order_price = pizza.price
        if formset.is_valid():
            for topping in formset.cleaned_data:  # topping to pojedynczy slownik, ktory sie zmienia co kazde przejscie
                if topping['number'] != None:
                    order_price += topping['price'] * topping['number']
            create_order = Order.objects.create(user=user, order_price=order_price)
            pizza_order = PizzaOrder.objects.create(pizza=pizza, order=create_order, amount=1)

            # create_order.pizzas.add(pizza_order)

            for topping in formset.cleaned_data:
                if topping['number'] != None:
                    topping_object = topping['id']
                    pizza_order_topping = PizzaOrderTops.objects.create(pizza_order=pizza_order, pizza_top=topping_object,
                                                                        amount=topping['number'])
            #
            #         pizza_order.toppings.add(pizza_order_topping)
        context = {
                    'pizza': pizza,
                    'formset': formset,
        }
        return render(request, self.template_name, context)

    # breakpoint()
