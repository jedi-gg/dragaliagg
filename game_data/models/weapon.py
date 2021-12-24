from django.conf import settings
from django.db import models

from game_data.utils.save_image import save_image


class Weapon(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100)
    wiki_url = models.CharField(max_length=100)
    rarity = models.PositiveIntegerField()
    element = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    release_date = models.DateField(null=True, blank=True)

    def get_wiki_url(self):
        return '{}{}'.format(settings.BASE_WIKI_URL, self.wiki_url)

    def get_image(self, size=155):
        return '{}game_assets/weapons/{}_{}.png'.format(
            settings.STATIC_URL,
            self.id,
            size
        )

    def download_images(self):
        thumb_image_sizes = ['40', '60', '100', '155',]

        for size in thumb_image_sizes:
            url = '{}/thumb.php?f={}.png&width={}'.format(
                settings.BASE_WIKI_URL, self.id, size)
            path = '_static/game_assets/weapons/{}_{}.png'.format(
                self.id, size)
            
            save_image(url, path)

    def __str__(self):
        return self.name
