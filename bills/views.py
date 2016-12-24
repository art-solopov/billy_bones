from django.shortcuts import render
from django.views.generic import ListView

from .models import PaymentMethod


class PaymentMethodsList(ListView):
    model = PaymentMethod
    template_name = 'bills/payment_methods_list.html'
