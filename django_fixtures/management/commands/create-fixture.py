from django.core.management import BaseCommand

from django_fixtures.utils.create import create_fixture_for_model


class Command(BaseCommand):
    help = 'Generates a fixture file for the specified model'

    def add_arguments(self, parser):
        parser.add_argument('model', type=str, help='The model label that determines for which model the fixture file is created')
        parser.add_argument('--dev', action='store_true', help='Determines whether or not this is a dev fixture')

    def handle(self, *args, **options):
        model_label = options['model']
        dev = options['dev']

        create_fixture_for_model(model_label, dev)
