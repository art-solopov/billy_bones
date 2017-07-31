from collections import OrderedDict
from datetime import datetime as dt

import arrow
from django.db import models
from django.core.exceptions import ValidationError
from model_utils.models import TimeStampedModel
from django_fsm import FSMIntegerField, transition
from taggit.managers import TaggableManager


class PaymentMethod(models.Model):
    name = models.CharField(max_length=1500)

    def __str__(self):
        return self.name


class Bill(TimeStampedModel):
    # State machine
    STATES = OrderedDict([
        (1, 'new'),
        (50, 'paid')
    ])
    STATE_IDS = {name: i for i, name in STATES.items()}

    state_i = FSMIntegerField(default=STATE_IDS['new'])

    @transition(field='state_i', source='*', target=STATE_IDS['new'])
    def reset(self):
        pass

    @transition(field='state_i',
                source=STATE_IDS['new'], target=STATE_IDS['paid'])
    def pay(self):
        self.paid = dt.now()

    # State machine ended

    period = models.DateField(db_index=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(null=True, blank=True)

    paid = models.DateField(null=True, blank=True)

    payment_method = models.ForeignKey(
        'PaymentMethod',
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

    tags = TaggableManager(blank=True)

    @property
    def state(self):
        return self.STATES[self.state_i]

    def _days_diff_with_monthshift(self, field, months=0):
        now = arrow.now()
        val = arrow.get(getattr(self, field))
        return (now - val.shift(months=months)).days

    def is_close_to_due(self):
        # TODO: configure numeric variables
        if self.is_overdue():
            return False
        return (
            self._days_diff_with_monthshift('period', 1) > 0 or
            self._days_diff_with_monthshift('created') > 15
        )

    def is_overdue(self):
        return (
            self._days_diff_with_monthshift('period', 2) > 0 or
            self._days_diff_with_monthshift('created', 1) > 0
        )

    def clean(self):
        errors = {}
        if self.state != 'new':
            if not self.paid:
                errors['paid'] = "Paid must be present"
            if self.payment_method is None:
                errors['payment_method'] = "Payment method must be present"

        if errors:
            raise ValidationError(errors)
