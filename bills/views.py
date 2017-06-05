from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import (DeleteView, CreateView, UpdateView)
from django.core.exceptions import PermissionDenied
from django_fsm import can_proceed

from .models import PaymentMethod, Bill
from .filters import BillsFilter
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


class WithBillsTagsMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Bill.tags.values('name', 'slug')
        return context


class BillsList(WithBillsTagsMixin, ListView):
    model = Bill
    template_name = 'bills/bills_list.html'

    def get_queryset(self):
        queryset = Bill.objects.prefetch_related('payment_method', 'tags')\
                               .order_by('id')
        self.bills_filter = BillsFilter(self.request.GET, queryset=queryset)
        return self.bills_filter.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.prepare_filter_form()
        context['bills_filter'] = self.bills_filter
        return context

    def prepare_filter_form(self):
        f = self.bills_filter.form
        f.helper = self.bills_filter.get_form_helper()


class BillCUMixin(WithBillsTagsMixin):
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
    initial = {'state_i': models.Bill.STATE_IDS['new']}


class DeleteBill(DeleteView):
    model = models.Bill
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('bills:index')
