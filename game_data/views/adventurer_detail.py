from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from game_data.models import Adventurer


class AdventurerDetail(DetailView):
    model = Adventurer
    template_name = 'game_data/adventurer-detail.html'
    slug_url_kwarg = 'adventurer_slug'
    context_object_name = 'adventurer'

    def get_context_data(self, **kwargs):
        context = super(AdventurerDetail, self).get_context_data(**kwargs)

        comps = []
        for build in self.object.builds.filter(comp__parent_comp__isnull=True):
            comps.append(build.comp)

        context['comps'] = comps

        return context
