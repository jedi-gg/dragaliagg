from django.views.generic.detail import DetailView

from comps.models import CompSection


class CompSectionDetail(DetailView):
    model = CompSection
    template_name = 'comps/section.html'
    slug_url_kwarg = 'section_slug'

    def get_context_data(self, **kwargs):
        context = super(CompSectionDetail, self).get_context_data(**kwargs)

        return context
