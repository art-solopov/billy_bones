from django import template

register = template.Library()


@register.filter
def state_str(bill):
    # TODO add i18n and color
    return '<span class="bill-state bill-state-{0}">{1}</span>'.format(
        bill.state, bill.state.upper())


@register.filter
def transition_str(transition):
    # TODO add i18n and color
    return transition.name.capitalize()


@register.filter
def tag_names(bill):
    return ', '.join(t.name for t in bill.tags.all())
