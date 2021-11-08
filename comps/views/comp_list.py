from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from comps.models import Comp, CompQuest, CompSection, CompDifficulty


class CompList(ListView):
    template_name = 'comps/comp-list.html'
    context_object_name = 'comps'
    object_type = None
    section = None
    section_slug = None
    quest = None
    quest_slug = None
    difficulty = None
    difficulty_slug = None

    def dispatch(self, request, *args, **kwargs):
        if 'section_slug' in kwargs:
            self.list_type = 'section'
            self.section_slug = kwargs['section_slug']

        if 'quest_slug' in kwargs:
            self.list_type = 'quest'
            self.quest_slug = kwargs['quest_slug']

        if 'difficulty_slug' in kwargs:
            self.list_type = 'difficulty'
            self.difficulty_slug = kwargs['difficulty_slug']

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        q = Q()
        if self.section_slug:
            self.section = get_object_or_404(CompSection, slug=self.section_slug)
            q &= Q(section=self.section)

        if self.quest_slug:
            self.quest = get_object_or_404(CompQuest, slug=self.quest_slug)
            q &= Q(quest=self.quest)
        
        if self.difficulty_slug:
            self.difficulty = get_object_or_404(CompDifficulty, slug=self.difficulty_slug)
            q &= Q(difficulty=self.difficulty)

        return Comp.objects.filter(q)

    def get_context_data(self, **kwargs):
        context = super(CompList, self).get_context_data(**kwargs)

        title_map = {
            'section': getattr(self, 'section', None),
            'quest': getattr(self, 'quest', None),
            'difficulty': '{} {}'.format(
                getattr(self, 'difficulty', ''),
                getattr(self, 'quest', ''),
            )
        }

        context['list_type'] = self.list_type
        context['title'] = title_map[self.list_type]
        context['section'] = self.section
        context['quest'] = self.quest
        context['difficulty'] = self.difficulty

        return context
