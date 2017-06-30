import django_filters
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Div, Submit, Field

from .models import Bill


class BillsFilter(django_filters.FilterSet):
    state_i__in = django_filters.TypedMultipleChoiceFilter(
        name='state_i',
        label='State',
        lookup_expr='in',
        coerce=int,
        choices=list(Bill.STATES.items())
    )
    tags__name__in = django_filters.MultipleChoiceFilter(
        name='tags__name',
        label='Tags',
        lookup_expr='in',
        choices=[(x.name, x.name) for x in Bill.tags.all()]
    )

    class Meta:
        model = Bill
        fields = {
            'cost': ['lte', 'gte'],
            'period': ['lte', 'gte'],
            'paid': ['lte', 'gte'],
            'tags__name': ['in'],
        }

    @staticmethod
    def get_form_helper():
        fh = FormHelper()
        fh.form_method = 'GET'
        fh.layout = Layout(
            # Since the form starts invisible, we have to set the selects'
            # widths manually
            Div(
                Field('state_i__in', wrapper_class='col-sm-12',
                      style='width: 100%'),
                css_class='row'
            ),
            Div(
                Field('cost__lte', wrapper_class='col-sm-12 col-md-6'),
                Field('cost__gte', wrapper_class='col-sm-12 col-md-6'),
                css_class='row'
            ),
            Div(
                Field('period__lte', wrapper_class='col-sm-12 col-md-6'),
                Field('period__gte', wrapper_class='col-sm-12 col-md-6'),
                css_class='row'
            ),
            Div(
                Field('paid__lte', wrapper_class='col-sm-12 col-md-6'),
                Field('paid__gte', wrapper_class='col-sm-12 col-md-6'),
                css_class='row'
            ),
            Div(
                Field('tags__name__in', wrapper_class='col-sm-12',
                      style='width: 100%'),
                css_class='row'
            ),
            Div(
                Div(Submit('search', 'Search'), css_class='col-sm-12'),
                css_class='row'
            )
        )
        return fh
