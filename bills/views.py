from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import (DeleteView, CreateView, UpdateView)
from django.core.exceptions import PermissionDenied
from django_fsm import can_proceed

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


class DeletePaymentMethod(DeleteView):
    model = models.PaymentMethod
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('bills:payment_methods:index')


class BillsList(ListView):
    model = Bill
    template_name = 'bills/bills_list.html'
    queryset = Bill.objects.prefetch_related('payment_method')


class BillCUMixin:
    template_name = 'bills/bill_form.html'
    model = models.Bill
    form_class = forms.BillForm
    success_url = reverse_lazy('bills:index')


class EditBill(BillCUMixin, UpdateView):
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if self.transition:
            transition = getattr(obj, self.transition)
            if can_proceed(transition):
                transition()
            else:
                raise PermissionDenied
        return obj

    @property
    def transition(self):
        return self.kwargs.get('action', None)


class CreateBill(BillCUMixin, CreateView):
    initial = {'state_i': 1}


class DeleteBill(DeleteView):
    model = models.Bill
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('bills:index')
