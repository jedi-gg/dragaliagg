from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from comps.models import Comp
from core.mixins import CacheMixin

class CompDetail(CacheMixin, DetailView):
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
            ('Comp Type', self.object.comp_type),
            ('Creator', self.object.creator),
            ('Date Posted', self.object.post_date),
            ('Game Version', self.object.game_version),
            ('Auto-Shapeshift', auto_shapeshift),
            ('Creator\'s Clear Time', self.object.get_clear_time),
            ('Creator\'s Clear Rate', self.object.get_clear_rate),
        ]

        if self.object.helper:
            helper_text = 'Helper'
            if self.object.helper_dragon:
                helper_text = '{} - {}'.format(
                    helper_text, self.object.helper_dragon)
            context['helper_text'] = helper_text

        return context
