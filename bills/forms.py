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
        exclude = ['state_i']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._adjust_validations()

    def _adjust_validations(self):
        instance = self.instance
        if instance.state != 'new':
            self.fields['paid'].required = True
        if instance.state == 'printed':
            self.fields['printed'].required = True
