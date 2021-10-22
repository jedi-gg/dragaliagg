import os
from django.apps import apps
from django.conf import settings
from django.core.management import call_command


def create_fixture_for_model(model_label, dev):
    """
    Creates a fixture file for the specified model
    """
    options = {
        'indent': 2,
        'use_natural_foreign_keys': True,
        'format': 'json'
    }
    if dev:
        options['use_natural_primary_keys'] = True

    path, file_name = get_fixture_path(model_label, dev)
    options['output'] = os.path.join(path, file_name)

    if not os.path.isdir(path):
        os.makedirs(path)

    call_command('dumpdata', model_label, **options)

def get_fixture_path(model_label, dev=False):
    """
    Returns the path and filename for a fixture
    """
    model = apps.get_model(model_label)

    file_name = f'{model._meta.object_name}.json'
    path = os.path.join(
        settings.BASE_DIR,
        settings.FIXTURES_DIR_NAME,
        settings.FIXTURES_DEV_DIR_NAME if dev else '',
        model._meta.app_label
    )

    return path, file_name
