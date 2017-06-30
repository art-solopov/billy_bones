import calendar
from datetime import date

from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Div, Row, Submit

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
        fields = ['tags', 'cost']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._adjust_validations()
        self.helper = FormHelper(self)
        self.helper.form_class = 'bills-bill-form'
        layout = self._build_fields()
        layout.fields.append(Submit('submit', 'Submit'))
        self.helper.layout = layout

    def save(self):
        self.instance.period = date(
            self.cleaned_data['period_year'],
            self.cleaned_data['period_month'],
            1
        )
        return super().save()

    def _adjust_validations(self):
        pass

    def _adjust_initials(self):
        period = self.instance.period or date.today()
        self.fields['period_month'].initial = period.month
        self.fields['period_year'].initial = period.year

    def _build_fields(self):
        return Layout(
            'tags',
            Row(
                Div('period_month', css_class='col-sm-12 col-md-4'),
                Div('period_year', css_class='col-sm-12 col-md-4'),
            ),
            Row(
                # TODO: add currency
                Div('cost', css_class='col-sm-12 col-md-3')
            )
        )


class PaidBillForm(BillForm):
    class Meta:
        model = models.Bill
        fields = BillForm.Meta.fields + ['payment_method', 'paid']

    def _adjust_validations(self):
        self.fields['paid'].required = True
        self.fields['payment_method'].required = True

    def _build_fields(self):
        layout = super()._build_fields()
        cost_row = layout.fields[-1]
        cost_row.fields.append(
            Div('paid', css_class='col-sm-12 col-md-6')
        )
        layout.append(
            'payment_method'
        )
        return layout
