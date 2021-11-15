from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from comps.models import CompCreator
from core.mixins import CacheMixin


class CreatorDetail(CacheMixin, ListView):
    template_name = 'comps/creator-detail.html'
    context_object_name = 'comps'
    paginate_by = 20
    creator = None

    def get_queryset(self):
        self.creator = get_object_or_404(CompCreator, slug=self.kwargs['slug'])
        return self.creator.comps.all()
    
    def get_context_data(self, **kwargs):
        context = super(CreatorDetail, self).get_context_data(**kwargs)

        context['creator'] = self.creator

        return context

