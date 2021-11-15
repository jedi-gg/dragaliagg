from django.db.models import Count
from django.views.generic.list import ListView

from comps.models import CompCreator
from core.mixins import CacheMixin


class CreatorList(CacheMixin, ListView):
    model = CompCreator
    template_name = 'comps/creator-list.html'
    context_object_name = 'creators'
    paginate_by = 20
    creator = None

    def get_queryset(self):
        return (
            CompCreator.objects
            .annotate(build_count=Count('comps'))
            .order_by('-build_count')
        )

