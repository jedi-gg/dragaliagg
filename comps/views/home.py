from datetime import datetime, timedelta


from django.views.decorators.cache import cache_page
from django.views.generic.list import ListView

from comps.models import Comp, CompQuest
from core.mixins import CacheMixin


class Home(CacheMixin, ListView):
    template_name = 'comps/home.html'
    context_object_name = 'comps'
    paginate_by = 20

    def get_queryset(self):
        return Comp.objects.all().order_by('-created_date')

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        last_month = datetime.today() - timedelta(days=30)

        # for comps in Comp.objects.filter(created_date__gte=last_month):
        #     print(comps)

        return context
