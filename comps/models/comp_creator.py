from django.db import models

from core.models import SlugModel


class CompCreator(SlugModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    creator_link_1 = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
