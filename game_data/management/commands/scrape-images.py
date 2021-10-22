import requests

from django.core.management.base import BaseCommand

from game_data.models import Adventurer

# Disable warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()


class Command(BaseCommand):
    def handle(self, *args, **options):
        for a in Adventurer.objects.all():
            a.download_images()
