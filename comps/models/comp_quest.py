from django.conf import settings
from django.db import models
from django.urls import reverse

from comps.enums import ElementEnum
from core.models import SlugModel


class CompQuest(SlugModel):
    title = models.CharField(max_length=100)
    nav_title = models.CharField(max_length=100, blank=True, null=True)
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    element = models.PositiveSmallIntegerField(choices=ElementEnum.as_tuples(), blank=True, null=True)
    ordering = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    wiki_link = models.URLField(blank=True, null=True)
    is_new = models.BooleanField(blank=True, default=False)
    image_offset = models.IntegerField(default=0)

    section = models.ForeignKey('CompSection', related_name='quests', on_delete=models.DO_NOTHING, blank=True, null=True)
    difficulties = models.ManyToManyField('CompDifficulty')

    def quest_slug(self):
        return self.slug

    def slug_name(self):
        return self.title
    
    def get_nav_title(self):
        return self.nav_title if self.nav_title else self.title
    
    def get_element(self):
        return ElementEnum(self.element).name

    def get_banner_image(self, size=250):
        return '{}game_assets/banners/{}.png'.format(
            settings.STATIC_URL,
            self.banner_title,
            # size
        )
    
    def get_absolute_url(self):
        return reverse('comp-list', kwargs={
            'section_slug': self.section.slug,
            'quest_slug': self.slug,
        })
        
    def __str__(self):
        return self.title
