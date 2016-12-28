from django.conf.urls import url

from .views import PaymentMethodsList, BillsList

urlpatterns = [
    url(r'payment_methods/?$', PaymentMethodsList.as_view(), name='payment_methods_index'),
    url(r'bills/?$', BillsList.as_view(), name='bills_index')
]
