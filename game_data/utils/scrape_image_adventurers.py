from game_data.models import Adventurer
from .save_image import save_image


def scrape_image_adventurers():
    thumb_image_sizes = ['40', '80', '120',]
    portrait_sizes = ['100', '200', '450', '1000',]
    for a in Adventurer.objects.all()[:10]:
        for size in thumb_image_sizes:
            url = 'https://dragalialost.wiki/thumb.php?f={}&width={}'.format(
                a.image, size)
            path = '_static/game_assets/adventurers/{}_{}.png'.format(
                a.image.replace('.png', ''), size)
            
            save_image(url, path)
        
        for size in portrait_sizes:
            url = 'https://dragalialost.wiki/thumb.php?f={}_portrait.png&width={}'.format(
                a.image.replace('.png', ''), size)
            path = '_static/game_assets/adventurers/{}_portrait_{}.png'.format(
                a.image.replace('.png', ''), size)
            
            save_image(url, path)
