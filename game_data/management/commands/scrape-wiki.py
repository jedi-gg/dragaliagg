from bs4 import BeautifulSoup
import requests

from django.core.management.base import BaseCommand

# Disable warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


class Command(BaseCommand):
    def handle(self, *args, **options):
        base_url = 'https://dragalialost.wiki/w/'

        # Scape Units
        url = "{}Adventurer_List".format(base_url)
        r = requests.get(url, verify=False)

        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html5lib")
            units = soup.findAll(
                'tr', {'class': 'character-grid-entry'}
            )

            unit_dict = {}
            for unit in units[:10]:
                unit_info = {}
                cols = unit.findAll('td')

                # for x, col in enumerate(cols, 0):
                #     print(x)
                #     print(col)

                unit_info['url'] = cols[0].find('a')['href']
                unit_info['image'] = cols[0].find('img')['src']
                unit_info['name'] = cols[1].find('a').text.strip()
                unit_info['rarity'] = cols[2].find('div').text.strip()
                unit_info['element'] = cols[3].find('div').text.strip()
                unit_info['weapon'] = cols[4].find('div').text.strip()
                # unit_dict[cols[0].string] = cols[1].string

                print(unit_info)
