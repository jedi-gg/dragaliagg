import os
from core import settings

# Remove when live
ALLOWED_HOSTS = ['dragalia.gg',]

STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(settings.BASE_DIR, "_static"),
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
