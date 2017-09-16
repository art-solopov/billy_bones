from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import (CreateView, UpdateView)

from .models import Note


class ListNotes(ListView):
    template_name = 'notes/list.html'
    queryset = Note.objects.order_by('note_type', 'created')


class CUMixin:
    model = Note
    fields = ['note_type', 'title', 'text']
    success_url = reverse_lazy('notes:index')

class CreateNote(CUMixin, CreateView):
    template_name = 'notes/create.html'

class UpdateNote(CUMixin, UpdateView):
    template_name = 'notes/update.html'
