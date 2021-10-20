from django.db import models


class Dragon(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    wiki_url = models.CharField(max_length=100)
    rarity = models.PositiveIntegerField()
    element = models.CharField(max_length=50)
