from django.forms import ModelForm

from . import models


class PaymentMethodForm(ModelForm):
    class Meta:
        model = models.PaymentMethod
        fields = [
            'name'
        ]


class BillForm(ModelForm):
    class Meta:
        model = models.Bill
        fields = [
            'period',
            'cost',
            'comment',
            'payment_method',
            'paid',
            'printed',
        ]
