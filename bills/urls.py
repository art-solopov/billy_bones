from django.conf.urls import url

from .views import PaymentMethodsList

urlpatterns = [
    url(r'payment_methods/?$', PaymentMethodsList.as_view(), name='payment_methods_index')
]
