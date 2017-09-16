from django.conf.urls import url

from .views import (ListNotes, CreateNote)

app_name = 'notes'

urlpatterns = [
    url(r'^$', ListNotes.as_view(), name='index'),
    url(r'^new$', CreateNote.as_view(), name='new'),
]
