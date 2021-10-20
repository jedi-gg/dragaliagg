from django.db import models


class Wyrmprint(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    wiki_url = models.CharField(max_length=100)
    rarity = models.PositiveIntegerField()
