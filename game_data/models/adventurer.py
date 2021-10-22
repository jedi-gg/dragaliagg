from django.conf import settings
from django.db import models

from game_data.utils.save_image import save_image


class Adventurer(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100)
    wiki_url = models.CharField(max_length=100)
    rarity = models.PositiveIntegerField()
    element = models.CharField(max_length=50)
    weapon = models.CharField(max_length=50)

    def get_image(self, size=60):
        return '{}game_assets/adventurers/{}_{}.png'.format(
            settings.STATIC_URL,
            self.id,
            size
        )
    
    def get_portrait(self, size=200):
        return '{}game_assets/adventurers/{}_portrait_{}.png'.format(
            settings.STATIC_URL,
            self.id,
            size
        )
    
    def download_images(self):
        thumb_image_sizes = ['40', '60', '80', '120',]
        portrait_sizes = ['100', '200', '450', '1000',]

        for size in thumb_image_sizes:
            url = '{}/thumb.php?f={}_r0{}.png&width={}'.format(
                settings.BASE_WIKI_URL, self.id, self.rarity, size)
            path = '_static/game_assets/adventurers/{}_{}.png'.format(
                self.id, size)
            
            save_image(url, path)
        
        for size in portrait_sizes:
            url = '{}/thumb.php?f={}_r05_portrait.png&width={}'.format(
                settings.BASE_WIKI_URL, self.id, size)
            path = '_static/game_assets/adventurers/{}_portrait_{}.png'.format(
                self.id, size)
            
            save_image(url, path)


    def __str__(self):
        return self.name
