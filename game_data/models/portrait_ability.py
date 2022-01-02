from django.conf import settings
from django.db import models
from django.utils.html import html_safe


@html_safe
class PortraitAbility(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    ability_name = models.CharField(max_length=100, blank=True, null=True)
    ability_icon = models.CharField(max_length=100, blank=True, null=True)
    ability_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ability_name
    
    class Meta:
        verbose_name_plural = "Portrait Abilities"
