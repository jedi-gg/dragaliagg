import os
from core import settings


STATIC_ROOT = os.path.join(settings.BASE_DIR, '_static')
STATICFILES_DIRS = [
    os.path.join(settings.BASE_DIR, "static"),
]
