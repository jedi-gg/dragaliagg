from django.core.management import (
    BaseCommand,
    call_command,
)

from django_fixtures.utils.load import get_ordered_fixtures


class Command(BaseCommand):
    help = 'Loads all existing fixture files including dev fixtures if --dev'

    def add_arguments(self, parser):
        parser.add_argument('--dev', action='store_true', help='Determines whether or not to also run dev fixtures')

    def handle(self, *args, **options):
        dev = options['dev']

        # Load base fixtures first
        print('Loading base fixtures...')
        fixtures = get_ordered_fixtures(dev=False)
        if fixtures:
            call_command('loaddata', *fixtures)

        # Load dev fixtures next if --dev is used
        if dev:
            print('Loading dev fixtures...')
            fixtures = get_ordered_fixtures(dev=True)
            if fixtures:
                call_command('loaddata', *fixtures)
