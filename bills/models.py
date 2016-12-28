from django.db import models
from model_utils.models import TimeStampedModel


class PaymentMethod(models.Model):
    name = models.CharField(max_length=1500)


BILL_STATES = [
    (1, 'new'),
    (50, 'paid'),
    (99, 'printed')
]

BILL_STATES_DICT = {k: name for k, name in BILL_STATES}


class Bill(TimeStampedModel):
    period = models.DateField(db_index=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(null=True, blank=True)

    state_i = models.IntegerField(choices=BILL_STATES)

    paid = models.DateTimeField(null=True, blank=True)
    printed = models.DateTimeField(null=True, blank=True)

    payment_method = models.ForeignKey(
        'PaymentMethod',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
