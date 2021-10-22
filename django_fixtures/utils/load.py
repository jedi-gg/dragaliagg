import os
from django.conf import settings


def get_all_fixtures(dev):
    """
    Returns a full list of all base or dev fixture files
    """
    fixtures = []
    fixtures_path = os.path.join(
        settings.BASE_DIR,
        settings.FIXTURES_DIR_NAME,
        settings.FIXTURES_DEV_DIR_NAME if dev else '',
    )
    app_labels = os.listdir(fixtures_path)

    # If there is a dev directory, remove it from app_labels
    if settings.FIXTURES_DEV_DIR_NAME in app_labels:
        app_labels.remove(settings.FIXTURES_DEV_DIR_NAME)

    for app_label in app_labels:
        app_label_path = os.path.join(fixtures_path, app_label)
        model_files = os.listdir(app_label_path)
        for model_file in model_files:
            fixtures.append(os.path.join(app_label_path, model_file))

    return fixtures

def get_ordered_fixtures(dev):
    """
    Some fixtures are required to be run before others for dependency reasons.
    This returns a list of base or dev fixture files such that all models listed in the
    FIXTURES_LIST settings are listed first and in the order that they are listed. Fixtures
    that are not listed in the settings are included last.
    """
    ordered_fixtures = []

    if dev:
        fixtures_list = settings.FIXTURES_LIST_DEV
    else:
        fixtures_list = settings.FIXTURES_LIST_BASE

    fixtures = get_all_fixtures(dev)

    # Add full fixture paths to ordered_fixtures based on the order defined in the settings
    for app_model in fixtures_list:
        for fixture in fixtures:
            app_model_file = app_model.replace('.', '/') + '.json'
            if app_model_file in fixture:
                ordered_fixtures.append(fixture)


    # Add all fixture paths to ordered_fixtures that are not mentioned in the Settings
    for fixture in fixtures:
        if fixture not in ordered_fixtures:
            ordered_fixtures.append(fixture)

    return ordered_fixtures
