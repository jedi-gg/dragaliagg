from .django import *
from .site import *

"""
If applicable, import local settings.
"""
try:
    from ._local import *
except ImportError:
    pass
