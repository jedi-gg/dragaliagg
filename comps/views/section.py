from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from comps.models import Comp, CompSection, CompQuest


class CompSectionList(ListView):
    model = CompQuest
    template_name = 'comps/section.html'
    slug_url_kwarg = 'section_slug'
    section = None
    context_object_name = 'comps'

    def get_queryset(self):
        self.section = get_object_or_404(CompSection, slug=self.kwargs['section_slug'])
        return Comp.objects.filter(section=self.section).order_by('-post_date')

    def get_context_data(self, **kwargs):
        context = super(CompSectionList, self).get_context_data(**kwargs)

        context['section'] = self.section

        return context
