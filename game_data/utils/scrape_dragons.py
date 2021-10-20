from bs4 import BeautifulSoup
import requests

from django.conf import settings
from django.utils.text import slugify

from game_data.models import Dragon


def scrape_dragons():
    # Dragon Lookup
    d_lookup = {}
    for d in Dragon.objects.all():
        d_lookup[d.slug] = ''

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

            name = cols[1].find('a').text.strip()
            slug = slugify(name)

            # Check if already in DB
            if slug in d_lookup:
                continue

            obj, created = Dragon.objects.get_or_create(
                name=name,
                defaults={
                    'slug': slug,
                    'image': cols[0].find('img')['src'].replace('/thumb.php?f=', '').replace('&width=80', ''),
                    'wiki_url': cols[0].find('a')['href'],
                    'rarity': cols[2].find('div').text.strip(),
                    'element': cols[3].find('div').text.strip(),
                }
            )

            if created:
                new_objs.append(obj)
        
        print('Created {} new Dragons'.format(len(new_objs)))
