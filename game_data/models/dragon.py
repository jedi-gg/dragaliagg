from django.conf import settings
from django.db import models

from game_data.utils.save_image import save_image


class Dragon(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    wiki_url = models.CharField(max_length=100)
    rarity = models.PositiveIntegerField()
    element = models.CharField(max_length=50)

    def get_wiki_url(self):
        return '{}{}'.format(settings.BASE_WIKI_URL, self.wiki_url)

    def get_image(self, size=155):
        return '{}game_assets/dragons/{}_{}.png'.format(
            settings.STATIC_URL,
            self.id,
            size
        )

    def download_images(self):
        thumb_image_sizes = ['60', '100', '155',]

        for size in thumb_image_sizes:
            url = '{}/thumb.php?f={}_01.png&width={}'.format(
                settings.BASE_WIKI_URL, self.id, size)
            path = '_static/game_assets/dragons/{}_{}.png'.format(
                self.id, size)
            
            save_image(url, path)

    def __str__(self):
        return self.name
