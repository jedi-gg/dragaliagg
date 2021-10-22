from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from comps.models import CompQuest


class CompQuestList(ListView):
    template_name = 'comps/quest.html'
    slug_url_kwarg = 'quest_slug'

    def get_queryset(self):
        self.quest = get_object_or_404(CompQuest, slug=self.kwargs['quest_slug'])
        return CompQuest.objects.filter(slug=self.kwargs['quest_slug'])

    def get_context_data(self, **kwargs):
        context = super(CompQuestList, self).get_context_data(**kwargs)

        context['quest'] = self.quest

        return context
