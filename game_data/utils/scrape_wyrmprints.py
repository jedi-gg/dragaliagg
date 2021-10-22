from bs4 import BeautifulSoup
import requests

from django.conf import settings
from django.utils.text import slugify

from game_data.models import Wyrmprint


def scrape_wyrmprints():
    # # Wyrmprint Lookup
    wp_lookup = {}
    for wp in Wyrmprint.objects.all():
        wp_lookup[wp.id] = ''

    # Scape Wyrmprints
    url = "{}/w/Wyrmprint_List".format(settings.BASE_WIKI_URL)
    r = requests.get(url, verify=False)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html5lib")
        trs = soup.findAll(
            'tr', {'class': 'wyrmprint-grid-entry'}
        )

        new_objs = []
        for row in trs:
            cols = row.findAll('td')

            wp_id = (
                cols[0].find('img')['src']
                .replace('/thumb.php?f=', '')
                .replace('_01.png&width=80', '')
                .replace('_02.png&width=80', '')
            )
            name = cols[1].find('a').text.strip()
            print('Creating {}'.format(name))
            ability_icon = row['data-ability-icon'].replace('Icon_Ability_', '')
            last_tooltip = row.find('td', {'class': 'wyrmprint-grid-entry-ability1'}).find_all('span', {'class': 'tooltip'})[-1]
            ability_name = last_tooltip.find('a').text
            ability_description = last_tooltip.find('span').text

            # Check if already in DB
            if wp_id in wp_lookup:
                continue

            obj, created = Wyrmprint.objects.get_or_create(
                id=wp_id,
                defaults={
                    'name': name,
                    'slug': slugify(name),
                    'wiki_url': cols[0].find('a')['href'],
                    'rarity': cols[2].find('div').text.strip(),
                    'ability_name': ability_name,
                    'ability_icon': ability_icon,
                    'ability_description': ability_description,
                }
            )

            if created:
                new_objs.append(obj)
        
        print('Created {} new Wyrmprints'.format(len(new_objs)))
