"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1.views import (
    MainView,
    PizzaView,
    PizzaDetailsView,
    ToppingView,
    PizzaToppingsView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('main/', PizzaView.as_view(), name='pizza-list'),
    path('pizza/', PizzaView.as_view(), name='pizza-list'),
    path('pizza-details/<int:pk>/', PizzaDetailsView.as_view(), name='pizza-details'),
    path('topping/', ToppingView.as_view(), name='topping-list'),
    path('pizza_topping/<int:pk>/', PizzaToppingsView.as_view(), name='pizza-topping'),
]
