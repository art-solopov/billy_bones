from django import template
from django.utils.safestring import mark_safe
from yattag import Doc

register = template.Library()

_STATE_CLASSES = {
    'new': 'text-info',
    'paid': 'text-success'
}


@register.simple_tag
def bill_state(bill):
    # TODO add i18n
    color = _STATE_CLASSES.get(bill.state)
    span_classes = [
        'bill-state',
        'bill-state-{0}'.format(bill.state),
        color
    ]
    span_classes = ' '.join(filter(bool, span_classes))

    doc, tag, text = Doc().tagtext()
    with tag('span', klass=span_classes):
        text(bill.state.upper())

    return mark_safe(doc.getvalue())


@register.filter
def transition_str(transition):
    # TODO add i18n and color
    return transition.name.capitalize()


@register.filter
def tag_names(bill):
    return ', '.join(t.name for t in bill.tags.all())


_NOTIFS_GLYPHICON = 'glyphicon glyphicon-exclamation-sign'


def _bill_notifs(bill):
    if bill.state != 'paid' and bill.is_close_to_due():
        doc, tag, text = Doc().tagtext()
        with tag('span', klass=_NOTIFS_GLYPHICON + ' text-warning'):
            doc.attr('title', 'Bills is almost due')
        yield doc.getvalue()
    if bill.state != 'paid' and bill.is_overdue():
        doc, tag, text = Doc().tagtext()
        with tag('span', klass=_NOTIFS_GLYPHICON + ' text-danger'):
            doc.attr('title', 'Bill is overdue!')
        yield doc.getvalue()


@register.simple_tag
def bill_notifs(bill):
    return mark_safe("\n".join(x for x in _bill_notifs(bill) if bool(x)))
