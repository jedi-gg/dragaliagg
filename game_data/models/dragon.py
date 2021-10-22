from django.db import models


class Dragon(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    wiki_url = models.CharField(max_length=100)
    rarity = models.PositiveIntegerField()
    element = models.CharField(max_length=50)

    def __str__(self):
        return self.name
