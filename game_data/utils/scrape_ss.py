from bs4 import BeautifulSoup
import requests

from django.conf import settings
from django.utils.text import slugify

from game_data.models import Adventurer


def scrape_ss():
    # Adventurer Lookup
    adv_lookup = {}
    for adv in Adventurer.objects.all():
        adv_lookup[adv.id] = ''

    # Scape Shared Skills
    url = "{}/w/List_of_Shareable_Skills".format(settings.BASE_WIKI_URL)
    r = requests.get(url, verify=False)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "html5lib")
        trs = soup.findAll(
            'tr', {'class': 'character-grid-entry'}
        )

        new_objs = []
        for row in trs:
            cols = row.findAll('td')

            unit_name = row.find('td', {'class': 'character-grid-entry-name'}).text.strip()

            try:
                adventurer = Adventurer.objects.get(name=unit_name)
            except:
                print('MISS')
            
            adventurer.shared_skill_cost = row.find('td', {'class': 'character-grid-entry-skill-cost'}).text.strip()
            adventurer.shared_skill_name = row.find('td', {'class': 'character-grid-entry-skill-name'}).find_all("a")[-1].text.strip()
            adventurer.shared_skill_sp = row.find('td', {'class': 'character-grid-entry-skill-sp-cost'}).text.strip()
            adventurer.shared_skill_description = row.find('td', {'class': 'character-grid-entry-skill-effect'}).find("p").text.strip()

            adventurer.save()
        
        print('Saved Shared Skills')
