from django.conf.urls import url

from .views import (ListNotes)

app_name = 'notes'

urlpatterns = [
    url(r'^/?$', ListNotes.as_view(), name='index')
]
