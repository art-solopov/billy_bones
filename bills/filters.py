import django_filters
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
            'period': ['lte', 'gte', 'exact'],
            'paid': ['lte', 'gte'],
            'printed': ['lte', 'gte'],
            'tags__name': ['in'],
        }
