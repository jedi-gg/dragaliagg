from django.views.generic import TemplateView

from comps.models import Comp


class Home(TemplateView):
    template_name = 'comps/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        context['comps'] = Comp.objects.all().order_by('-post_date')

        return context
