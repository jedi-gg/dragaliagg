from django.db.models import Count
from django.views.generic.list import ListView

from game_data.models import Adventurer


class AdventurerList(ListView):
    model = Adventurer
    template_name = 'game_data/adventurer-list.html'
    context_object_name = 'adventurers'
    paginate_by = 16

    def get_queryset(self):
        return (
            Adventurer.objects.all()
            .annotate(build_count=Count('builds'))
            .order_by('-build_count')
        )

    def get_context_data(self, **kwargs):
        context = super(AdventurerList, self).get_context_data(**kwargs)

        return context
