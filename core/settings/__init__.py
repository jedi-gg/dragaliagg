from decouple import config

from .django import *
from .site import *
from .fixtures import *

"""
Import environment settings
"""
if config('ENV', default='DEV') == 'DEV':
    from ._dev import *

"""
If applicable, import local settings.
"""
try:
    from ._local import *
except ImportError:
    pass
