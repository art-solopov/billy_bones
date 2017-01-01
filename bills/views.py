from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import (DeleteView, CreateView, UpdateView,
                                       FormView)

from .models import PaymentMethod, Bill
from . import forms
from . import models


class PaymentMethodsList(ListView):
    template_name = 'bills/payment_methods_list.html'
    queryset = PaymentMethod.objects.order_by('name')


class PaymentMethodCUMixin:
    template_name = 'bills/payment_method_form.html'
    model = models.PaymentMethod
    form_class = forms.PaymentMethodForm
    success_url = reverse_lazy('bills:payment_methods:index')


class CreatePaymentMethod(PaymentMethodCUMixin, CreateView):
    pass


class EditPaymentMethod(PaymentMethodCUMixin, UpdateView):
    pass


class BillsList(ListView):
    model = Bill
    template_name = 'bills/bills_list.html'
    queryset = Bill.objects.prefetch_related('payment_method')
