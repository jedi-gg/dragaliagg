from django.views.generic.list import ListView

from comps.models import Comp


class Home(ListView):
    template_name = 'comps/home.html'
    context_object_name = 'comps'
    paginate_by = 20

    def get_queryset(self):
        return Comp.objects.all().order_by('-created_date')
