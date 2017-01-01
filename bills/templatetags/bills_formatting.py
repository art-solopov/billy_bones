from django import template
from ..models import BILL_STATES_DICT

register = template.Library()

@register.filter
def state_str(bill):
    # TODO add i18n and color
    return BILL_STATES_DICT[bill.state_i]
