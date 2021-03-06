from bs4 import BeautifulSoup
import datetime
import requests

from django.conf import settings
from django.utils.text import slugify

from game_data.models import Weapon


def scrape_weapons():
    # Weapon Lookup
    w_lookup = {}
    for w in Weapon.objects.all():
        w_lookup[w.id] = ''

    # Scape Weapons
    url = "{}/w/Weapon_List".format(settings.BASE_WIKI_URL)
    r = requests.get(url, verify=False)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html5lib")
        rows = soup.findAll(
            'tr', {'class': 'character-grid-entry'}
        )

        new_objs = []
        for row in rows:
            cols = row.findAll('td')

            w_id = cols[0].find('img')['alt'].replace(' ','_').replace('.png', '')
            name = cols[1].find('a').text.strip()

            release_date = datetime.datetime.strptime(
                cols[10].text.strip(), "%b %d, %Y").date()

            # Check if already in DB
            # if w_id in w_lookup:
            #     continue

            obj, created = Weapon.objects.update_or_create(
                id=w_id,
                defaults={
                    'name': name,
                    'slug': slugify(name),
                    'wiki_url': cols[0].find('a')['href'],
                    'rarity': cols[2].find('img')['title'],
                    'type': cols[3].find('img')['title'],
                    'element': cols[4].find('img')['title'],
                    'release_date': release_date,
                }
            )

            if created:
                new_objs.append(obj)
        
        print('Created {} new Weapons'.format(len(new_objs)))
