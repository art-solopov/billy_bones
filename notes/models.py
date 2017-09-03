from django.db import models
from model_utils.models import TimeStampedModel


class Note(TimeStampedModel):
    TYPE_CHOICES = (
        (1, 'Bill'),
    )

    note_type = models.IntegerField(choices=TYPE_CHOICES, db_index=True)
    title = models.CharField(max_length=511)
    text = models.TextField()

    class Meta:
        index_together = [
            ['note_type', 'created']
        ]
