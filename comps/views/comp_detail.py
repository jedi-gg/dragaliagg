from django.utils.safestring import mark_safe
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
        
        creator_markup = '<a href="{}">{}</a>'.format(
            self.object.creator.get_absolute_url(), self.object.creator
        )

        context['comp_data'] = [
            ('Comp Type', self.object.comp_type),
            ('Creator', mark_safe(creator_markup)),
            ('Date Posted', self.object.post_date),
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
