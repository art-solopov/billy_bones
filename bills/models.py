from collections import OrderedDict
from datetime import datetime as dt

from django.db import models
from django.core.exceptions import ValidationError
from model_utils.models import TimeStampedModel
from django_fsm import FSMIntegerField, transition


class PaymentMethod(models.Model):
    name = models.CharField(max_length=1500)

    def __str__(self):
        return self.name


class Bill(TimeStampedModel):
    # State machine
    STATES = OrderedDict([
        (1, 'new'),
        (50, 'paid'),
        (99, 'printed')
    ])
    STATE_IDS = { name: i for i, name in STATES.items() }

    state_i = FSMIntegerField(default=STATE_IDS['new'])

    @transition(field='state_i', source='*', target=STATE_IDS['new'])
    def reset(self):
        pass

    @transition(field='state_i',
                source=STATE_IDS['new'], target=STATE_IDS['paid'])
    def pay(self):
        self.paid = dt.now()

    @transition(field='state_i',
                source=STATE_IDS['paid'], target=STATE_IDS['printed'])
    def print(self):
        self.printed = dt.now()

    # State machine ended

    period = models.DateField(db_index=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(null=True, blank=True)

    paid = models.DateTimeField(null=True, blank=True)
    printed = models.DateTimeField(null=True, blank=True)

    payment_method = models.ForeignKey(
        'PaymentMethod',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    @property
    def state(self):
        return self.STATES[self.state_i]

    def clean(self):
        errors = {}
        if self.state != 'new':
            if not self.paid:
                errors['paid'] = "Paid must be present"
            if self.payment_method is None:
                errors['payment_method'] = "Payment method must be present"
        if self.state == 'printed':
            if not self.printed:
                errors['printed'] = "Printed must be present"

        if errors:
            raise ValidationError(errors)
