from django.views.generic.detail import DetailView

from comps.models import CompQuest


class CompQuestDetail(DetailView):
    model = CompQuest
    template_name = 'comps/quest.html'
    slug_url_kwarg = 'quest_slug'

    def get_context_data(self, **kwargs):
        context = super(CompQuestDetail, self).get_context_data(**kwargs)

        return context
