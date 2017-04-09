from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from . import models


class PaymentMethodForm(ModelForm):
    class Meta:
        model = models.PaymentMethod
        fields = [
            'name'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='btn btn-success')
        )


class BillForm(ModelForm):
    class Meta:
        model = models.Bill
        exclude = ['state_i']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._adjust_validations()
        self.helper = FormHelper(self)
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='btn btn-success')
        )

    def _adjust_validations(self):
        instance = self.instance
        if instance.state != 'new':
            self.fields['paid'].required = True
        if instance.state == 'printed':
            self.fields['printed'].required = True
