from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from comps.models import Comp, CompSection, CompQuest


class CompDetail(DetailView):
    model = Comp
    template_name = 'comps/comp.html'
    slug_url_kwarg = 'comp_slug'
    context_object_name = 'comp'

    def get_context_data(self, **kwargs):
        context = super(CompDetail, self).get_context_data(**kwargs)

        context['section'] = self.object.section

        auto_shapeshift = 'Off'
        if self.object.auto_shapeshift:
            auto_shapeshift = 'On'

        context['comp_data'] = [
            ('Creator', self.object.creator),
            ('Date Posted', self.object.post_date),
            ('Game Version', self.object.game_version),
            ('Auto-Shapeshift', auto_shapeshift),
            ('Creator\'s Clear Time', self.object.clear_time),
            ('Creator\'s Clear Rate', '{}%'.format(self.object.clear_rate)),
        ]

        return context
