# from django.shortcuts import render
from django.views.generic import ListView

from .models import Note


class ListNotes(ListView):
    template_name = 'notes/list.html'
    queryset = Note.objects.order_by('note_type', 'created')

# Create your views here.
