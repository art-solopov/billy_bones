from django.db import models
from django.contrib.contenttypes.models import ContentType


class Note(models.Model):
    content_type = models.ForeignKey(ContentType)
    text = models.TextField()
