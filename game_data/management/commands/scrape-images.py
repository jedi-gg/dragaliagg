import requests

from django.core.management.base import BaseCommand

from game_data.utils import (
    scrape_image_adventurers,
)

# Disable warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


class Command(BaseCommand):
    def handle(self, *args, **options):
        scrape_image_adventurers()

