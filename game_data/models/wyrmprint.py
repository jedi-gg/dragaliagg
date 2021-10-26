from django.conf import settings
from django.db import models

from game_data.utils.save_image import save_image


class Wyrmprint(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    image_id = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100)
    wiki_url = models.CharField(max_length=100)
    rarity = models.PositiveIntegerField()
    affinity_name = models.CharField(max_length=100, blank=True, null=True)
    affinity_icon = models.CharField(max_length=100, blank=True, null=True)
    ability_name = models.CharField(max_length=100, blank=True, null=True)
    ability_icon = models.CharField(max_length=100, blank=True, null=True)
    ability_description = models.TextField(blank=True, null=True)

    def download_images(self):
        thumb_image_sizes = ['30', '60', '155',]
        portrait_sizes = ['100', '200', '450', '1000',]

        for size in thumb_image_sizes:
            url = '{}/thumb.php?f={}_01.png&width={}'.format(
                settings.BASE_WIKI_URL, self.image_id, size)
            path = '_static/game_assets/wyrmprints/{}_{}.png'.format(
                self.image_id, size)
            
            save_image(url, path)
        
        # for size in portrait_sizes:
        #     url = '{}/thumb.php?f={}_r05_portrait.png&width={}'.format(
        #         settings.BASE_WIKI_URL, self.id, size)
        #     path = '_static/game_assets/adventurers/{}_portrait_{}.png'.format(
        #         self.id, size)
            
        #     save_image(url, path)

    def __str__(self):
        return '{} - {}'.format(self.name, self.ability_name)
