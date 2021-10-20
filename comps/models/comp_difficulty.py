from django.db import models

from core.models import SlugModel
from . import CompQuest

class CompDifficulty(SlugModel):
    title = models.CharField(max_length=100)
    ordering = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    quest = models.ForeignKey(CompQuest, related_name='difficulties', on_delete=models.DO_NOTHING, blank=True, null=True)

    def slug_name(self):
        return self.title

    def __str__(self):
        return '{0} - {1}'.format(self.quest.title, self.title)
