from django.conf import settings
from django.db import models


class Adventurer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    wiki_url = models.CharField(max_length=100)
    rarity = models.PositiveIntegerField()
    element = models.CharField(max_length=50)
    weapon = models.CharField(max_length=50)

    def get_image(self, size=80):
        return '{}game_assets/adventurers/{}_{}.png'.format(
            settings.STATIC_URL,
            self.image.replace('.png', ''),
            size
        )
    
    def get_portrait(self, size=200):
        return '{}game_assets/adventurers/{}_portrait_{}.png'.format(
            settings.STATIC_URL,
            self.image.replace('.png', ''),
            size
        )

    def __str__(self):
        return self.name
