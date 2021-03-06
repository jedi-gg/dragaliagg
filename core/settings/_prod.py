import os
from core import settings

# Remove when live
ALLOWED_HOSTS = ['dragalia.gg', 'dg.nginx',]

STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(settings.BASE_DIR, "_static"),
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

DEFAULT_CACHE_TIMEOUT = 604800
