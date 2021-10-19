from .django import *

"""
If applicable, import local settings.
"""
try:
    from ._local import *
except ImportError:
    pass
