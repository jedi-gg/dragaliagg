from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = 'Generates all fixtures from settings'

    def handle(self, *args, **options):
        for fixture in settings.FIXTURES_LIST_DEV_GAME:
            call_command('create-fixture', '--dev', fixture)
