from django.db import models
from django.urls import reverse

from core.models import SlugModel


class CompSection(SlugModel):
    title = models.CharField(max_length=100)
    nav_title = models.CharField(max_length=100, blank=True, null=True)
    ordering = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    wiki_link = models.URLField(blank=True, null=True)

    def slug_name(self):
        return self.title
    
    def string_slug(self):
        return self.slug.replace('-', '')
    
    def get_quests(self):
        return self.quests.order_by('ordering')
    
    def get_nav_title(self):
        return self.nav_title if self.nav_title else self.title

    def get_absolute_url(self):
        return reverse('section-list', kwargs={
            'section_slug': self.slug,
        })

    def __str__(self):
        return self.title