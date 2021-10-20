from django.db import models

from core.models import SlugModel


class CompSection(SlugModel):
    title = models.CharField(max_length=100)
    ordering = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    def slug_name(self):
        return self.title

    def __str__(self):
        return self.title