from django import template

register = template.Library()

@register.filter
def state_str(bill):
    # TODO add i18n and color
    return bill.state

@register.filter
def transition_str(transition):
    # TODO add i18n and color
    return transition.name.capitalize()
