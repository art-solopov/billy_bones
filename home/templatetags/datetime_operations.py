from django import template
import arrow

register = template.Library()

@register.filter(expects_localtime=True)
def format_period(date):
    return arrow.get(date).format('MMMM YYYY')

@register.filter(expects_localtime=True)
def format_date_long(date):
    if not date:
        return ''
    return arrow.get(date).format('DD MMMM YYYY')
