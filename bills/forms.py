import calendar
from datetime import date

from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Div, Submit

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
    period_month = forms.TypedChoiceField(
        choices=list(enumerate(calendar.month_name))[1:],
        coerce=int,
        empty_value=0
    )
    period_year = forms.IntegerField()

    class Meta:
        model = models.Bill
        exclude = ['period', 'state_i']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._adjust_validations()
        self._adjust_initials()
        self.helper = FormHelper(self)
        self.helper.form_class = 'bills-bill-form'
        self.helper.layout = Layout(
            Div(
                Div('period_month', css_class='col-sm-12 col-md-4'),
                Div('period_year', css_class='col-sm-12 col-md-4'),
                css_class='row'
            ),
            'cost',
            'paid',
            'printed',
            'tags',
            'payment_method',
            Submit('submit', 'Submit', css_class='btn btn-success')
        )

    def save(self):
        self.instance.period = date(
            self.cleaned_data['period_year'],
            self.cleaned_data['period_month'],
            1
        )
        return super().save()

    def _adjust_validations(self):
        instance = self.instance
        if instance.state != 'new':
            self.fields['paid'].required = True
        if instance.state == 'printed':
            self.fields['printed'].required = True

    def _adjust_initials(self):
        period = self.instance.period or date.today()
        self.fields['period_month'].initial = period.month
        self.fields['period_year'].initial = period.year
