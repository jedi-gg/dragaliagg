import requests

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from game_data.utils import (
    scrape_adventurers,
    scrape_wyrmprints,
    scrape_dragons,
    scrape_weapons,
)

# Disable warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


class Command(BaseCommand):
    def handle(self, *args, **options):
        scrape_adventurers()
        scrape_wyrmprints()
        scrape_dragons()
        scrape_weapons()
