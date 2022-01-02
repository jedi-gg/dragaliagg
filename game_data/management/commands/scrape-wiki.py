import requests

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from game_data.utils.scrape_adventurers import scrape_adventurers
from game_data.utils.scrape_wyrmprints import scrape_wyrmprints
from game_data.utils.scrape_weapons import scrape_weapons
from game_data.utils.scrape_dragons import scrape_dragons
from game_data.utils.scrape_ss import scrape_ss

# Disable warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


class Command(BaseCommand):
    def handle(self, *args, **options):
        scrape_adventurers()
        scrape_wyrmprints()
        scrape_dragons()
        scrape_weapons()
        scrape_ss()
