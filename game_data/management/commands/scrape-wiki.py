from bs4 import BeautifulSoup
import requests

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from game_data.models import Adventurer, Wyrmprint, Dragon

# Disable warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Adventurer Lookup
        adv_lookup = {}
        for adv in Adventurer.objects.all():
            adv_lookup[adv.slug] = ''
        
        # Wyrmprint Lookup
        wp_lookup = {}
        for wp in Wyrmprint.objects.all():
            wp_lookup[adv.slug] = ''
        
        # Dragon Lookup
        drg_lookup = {}
        for drg in Dragon.objects.all():
            drg_lookup[adv.slug] = ''

        base_url = 'https://dragalialost.wiki/w/'

        # Scape Units
        url = "{}Adventurer_List".format(base_url)
        r = requests.get(url, verify=False)

        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html5lib")
            units = soup.findAll(
                'tr', {'class': 'character-grid-entry'}
            )

            for unit in units:
                cols = unit.findAll('td')

                name = cols[1].find('a').text.strip()
                slug = slugify(name)

                # Check if already in DB
                if slug in adv_lookup:
                    continue

                Adventurer.objects.update_or_create(
                    name=name,
                    defaults={
                        'slug': slug,
                        'image': cols[0].find('img')['src'].replace('/thumb.php?f=', '').replace('&width=80', ''),
                        'wiki_url': cols[0].find('a')['href'],
                        'rarity': cols[2].find('div').text.strip(),
                        'element': cols[3].find('div').text.strip(),
                        'weapon': cols[4].find('div').text.strip()
                    }
                )
     
        # Scape Wyrmprints
        url = "{}Wyrmprint_List".format(base_url)
        r = requests.get(url, verify=False)

        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html5lib")
            trs = soup.findAll(
                'tr', {'class': 'wyrmprint-grid-entry'}
            )

            for row in trs:
                cols = row.findAll('td')

                name = cols[1].find('a').text.strip()
                slug = slugify(name)

                # Check if already in DB
                if slug in wp_lookup:
                    continue

                Wyrmprint.objects.update_or_create(
                    name=name,
                    defaults={
                        'slug': slug,
                        'image': cols[0].find('img')['src'].replace('/thumb.php?f=', '').replace('&width=80', ''),
                        'wiki_url': cols[0].find('a')['href'],
                        'rarity': cols[2].find('div').text.strip(),
                    }
                )
        
        # Scape Dragons
        url = "{}Dragon_List".format(base_url)
        r = requests.get(url, verify=False)

        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html5lib")
            trs = soup.findAll(
                'tr', {'class': 'character-grid-entry'}
            )

            for row in trs:
                cols = row.findAll('td')

                name = cols[1].find('a').text.strip()
                slug = slugify(name)

                # Check if already in DB
                if slug in drg_lookup:
                    continue

                Dragon.objects.update_or_create(
                    name=name,
                    defaults={
                        'slug': slug,
                        'image': cols[0].find('img')['src'].replace('/thumb.php?f=', '').replace('&width=80', ''),
                        'wiki_url': cols[0].find('a')['href'],
                        'rarity': cols[2].find('div').text.strip(),
                        'element': cols[3].find('div').text.strip(),
                    }
                )