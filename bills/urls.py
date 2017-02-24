from django.conf.urls import url, include

from .views import (PaymentMethodsList, EditPaymentMethod, CreatePaymentMethod,
                    DeletePaymentMethod,
                    BillsList, EditBill, DeleteBill, CreateBill)

app_name = 'bills'

payment_methods_patterns = [
    url(r'^$', PaymentMethodsList.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/edit/?$', EditPaymentMethod.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/?$', DeletePaymentMethod.as_view(),
        name='delete'),
    url(r'^new/?$', CreatePaymentMethod.as_view(), name='new'),
]

urlpatterns = [
    url(r'^payment_methods/', include((payment_methods_patterns, 'payment_methods'))),

    url(r'^bills(?:/(?P<tag>\w+)/?)?$', BillsList.as_view(), name='index'),
    url(r'^bills/(?P<pk>\d+)/edit(?:/(?P<action>\w+))?/?$', EditBill.as_view(), name='edit'),
    url(r'^bills/(?P<pk>\d+)/delete/?$', DeleteBill.as_view(), name='delete'),
    url(r'^bills/new/?$', CreateBill.as_view(), name='new'),
]
