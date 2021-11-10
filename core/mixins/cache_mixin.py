from django.conf import settings

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, cache_control, never_cache
from django.views.decorators.vary import vary_on_cookie


@method_decorator(vary_on_cookie, name='dispatch')
@method_decorator(cache_page(settings.DEFAULT_CACHE_TIMEOUT), name='dispatch')
@method_decorator(cache_control(must_revalidate=True, no_cache=True), name='dispatch')
class CacheMixin(object):
    cache_timeout = settings.DEFAULT_CACHE_TIMEOUT
    
    def dispatch(self, *args, **kwargs):
        return super(CacheMixin, self).dispatch(*args, **kwargs)
