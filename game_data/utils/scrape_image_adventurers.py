from game_data.models import Adventurer
from .save_image import save_image


def scrape_image_adventurers():
    thumb_image_sizes = ['40', '80', '120',]
    portrait_sizes = ['100', '200', '450', '1000',]
    for a in Adventurer.objects.all():
        for size in thumb_image_sizes:
            url = 'https://dragalialost.wiki/thumb.php?f={}_01_r0{}&width={}'.format(
                a.adventurer_id, a.rarity, size)
            path = '_static/game_assets/adventurers/{}_{}.png'.format(
                a.adventurer_id, size)
            
            save_image(url, path)
        
        for size in portrait_sizes:
            url = 'https://dragalialost.wiki/thumb.php?f={}_portrait.png&width={}'.format(
                a.adventurer_id, size)
            path = '_static/game_assets/adventurers/{}_portrait_{}.png'.format(
                a.adventurer_id, size)
            
            save_image(url, path)
