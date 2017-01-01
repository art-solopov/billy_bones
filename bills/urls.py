from django.conf.urls import url, include

from .views import (PaymentMethodsList, EditPaymentMethod, CreatePaymentMethod,
                    BillsList)

app_name = 'bills'

payment_methods_patterns = [
    url(r'^$', PaymentMethodsList.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/edit/?$', EditPaymentMethod.as_view(), name='edit'),
    url(r'^new/?$', CreatePaymentMethod.as_view(), name='new'),
]

urlpatterns = [
    url(r'^payment_methods/', include((payment_methods_patterns, 'payment_methods'))),
    
    url(r'^bills/?$', BillsList.as_view(), name='bills_index')
]
