from django.db import models

from core.models import SlugModel


class CompQuest(SlugModel):
    title = models.CharField(max_length=100)
    ordering = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    section = models.ForeignKey('CompSection', related_name='quests', on_delete=models.DO_NOTHING, blank=True, null=True)
    difficulties = models.ManyToManyField('CompDifficulty')

    def slug_name(self):
        return self.title
    
    def __str__(self):
        return self.title
