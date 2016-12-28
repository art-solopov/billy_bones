from django.shortcuts import render
from django.views.generic import ListView

from .models import PaymentMethod, Bill


class PaymentMethodsList(ListView):
    model = PaymentMethod
    template_name = 'bills/payment_methods_list.html'


class BillsList(ListView):
    model = Bill
    template_name = 'bills/bills_list.html'
    queryset = Bill.objects.prefetch_related('payment_method')
