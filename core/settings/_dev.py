import os
from core import settings

DEBUG = True

STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(settings.BASE_DIR, "_static"),
]

DEFAULT_CACHE_TIMEOUT = 0