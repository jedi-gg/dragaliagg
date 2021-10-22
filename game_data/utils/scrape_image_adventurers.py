import requests
import shutil

from django.conf import settings
from django.utils.text import slugify

from game_data.models import Adventurer


def scrape_image_adventurers():
    # Adventurer Lookup
    for a in Adventurer.objects.all()[:1]:
        print(a.image)

        url = 'https://dragalialost.wiki/thumb.php?f={}.png&width=80'
        response = requests.get(url, stream=True)
        with open('img.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

    # # Scape Adventurers
    # url = "{}/w/Adventurer_List".format(settings.BASE_WIKI_URL)
    # r = requests.get(url, verify=False)

    # if r.status_code == 200:
    #     soup = BeautifulSoup(r.content, "html5lib")
    #     units = soup.findAll(
    #         'tr', {'class': 'character-grid-entry'}
    #     )

    #     new_objs = []
    #     for unit in units:
    #         cols = unit.findAll('td')

    #         name = cols[1].find('a').text.strip()
    #         slug = slugify(name)

    #         # Check if already in DB
    #         if slug in adv_lookup:
    #             continue

    #         obj, created = Adventurer.objects.get_or_create(
    #             name=name,
    #             defaults={
    #                 'slug': slug,
    #                 'image': cols[0].find('img')['src'].replace('/thumb.php?f=', '').replace('&width=80', ''),
    #                 'wiki_url': cols[0].find('a')['href'],
    #                 'rarity': cols[2].find('div').text.strip(),
    #                 'element': cols[3].find('div').text.strip(),
    #                 'weapon': cols[4].find('div').text.strip()
    #             }
    #         )

    #         if created:
    #             new_objs.append(obj)
        
    #     print('Created {} new Adventurers'.format(len(new_objs)))
