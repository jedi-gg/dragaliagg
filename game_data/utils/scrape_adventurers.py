from bs4 import BeautifulSoup
import requests

from django.conf import settings
from django.utils.text import slugify

from game_data.models import Adventurer


def scrape_adventurers():
    # Adventurer Lookup
    adv_lookup = {}
    for adv in Adventurer.objects.all():
        adv_lookup[adv.id] = ''

    # Scape Adventurers
    url = "{}/w/Adventurer_List".format(settings.BASE_WIKI_URL)
    r = requests.get(url, verify=False)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html5lib")
        units = soup.findAll(
            'tr', {'class': 'character-grid-entry'}
        )

        new_objs = []
        for unit in units:
            cols = unit.findAll('td')

            id_parts = cols[0].find('img')['alt'].split(' ')
            adv_id = '{}_{}'.format(id_parts[0], id_parts[1])
            name = cols[1].find('a').text.strip()

            # Check if already in DB
            if adv_id in adv_lookup:
                continue

            obj, created = Adventurer.objects.get_or_create(
                id = adv_id,
                defaults={
                    'name': name,
                    'slug': slugify(name),
                    'wiki_url': cols[0].find('a')['href'],
                    'rarity': cols[2].find('div').text.strip(),
                    'element': cols[3].find('div').text.strip(),
                    'weapon': cols[4].find('div').text.strip()
                }
            )

            if created:
                new_objs.append(obj)
        
        print('Created {} new Adventurers'.format(len(new_objs)))
