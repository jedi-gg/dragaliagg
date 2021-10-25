from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from comps.models import Comp, CompQuest


class CompQuestList(ListView):
    template_name = 'comps/quest.html'
    slug_url_kwarg = 'quest_slug'
    context_object_name = 'comps'

    def get_queryset(self):
        self.quest = get_object_or_404(CompQuest, slug=self.kwargs['quest_slug'])
        return Comp.objects.filter(quest=self.quest)

    def get_context_data(self, **kwargs):
        context = super(CompQuestList, self).get_context_data(**kwargs)

        context['quest'] = self.quest
        context['banner'] = self.quest.get_banner_image()

        return context
