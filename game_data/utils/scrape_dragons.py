from bs4 import BeautifulSoup
import requests

from django.conf import settings
from django.utils.text import slugify

from game_data.models import Dragon


def scrape_dragons():
    # Dragon Lookup
    d_lookup = {}
    for d in Dragon.objects.all():
        d_lookup[d.id] = ''

    # Scape Dragons
    url = "{}/w/Dragon_List".format(settings.BASE_WIKI_URL)
    r = requests.get(url, verify=False)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html5lib")
        trs = soup.findAll(
            'tr', {'class': 'character-grid-entry'}
        )

        new_objs = []
        for row in trs:
            cols = row.findAll('td')

            id_parts = cols[0].find('img')['alt'].split(' ')
            d_id = id_parts[0]
            name = cols[1].find('a').text.strip()

            # Check if already in DB
            if d_id in d_lookup:
                continue

            obj, created = Dragon.objects.get_or_create(
                id=d_id,
                defaults={
                    'name': name,
                    'slug': slugify(name),
                    'wiki_url': cols[0].find('a')['href'],
                    'rarity': cols[2].find('div').text.strip(),
                    'element': cols[3].find('div').text.strip(),
                }
            )

            if created:
                new_objs.append(obj)
        
        print('Created {} new Dragons'.format(len(new_objs)))
