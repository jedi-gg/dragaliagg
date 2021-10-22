from django.db import models


class Wyrmprint(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100)
    wiki_url = models.CharField(max_length=100)
    rarity = models.PositiveIntegerField()
    affinity_name = models.CharField(max_length=100, blank=True, null=True)
    affinity_icon = models.CharField(max_length=100, blank=True, null=True)
    ability_name = models.CharField(max_length=100, blank=True, null=True)
    ability_icon = models.CharField(max_length=100, blank=True, null=True)
    ability_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
