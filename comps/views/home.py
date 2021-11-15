from django.views.generic.list import ListView

from comps.models import Comp
from core.mixins import CacheMixin


class Home(CacheMixin, ListView):
    template_name = 'comps/home.html'
    context_object_name = 'comps'
    paginate_by = 20

    def get_queryset(self):
        return Comp.list_objects.order_by('-created_date')
