from decouple import config

from .django import *
from .site import *
from .fixtures import *
from .aws import *

"""
Import environment settings
"""
if config('ENV', default='DEV') == 'DEV':
    from ._dev import *

if config('ENV', default='DEV') == 'PROD':
    from ._prod import *
    from .sentry import *

"""
If applicable, import local settings.
"""
try:
    from ._local import *
except ImportError:
    pass
