
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from core.models import SiteFAQ


class SiteFAQList(ListView):
    model = SiteFAQ
    template_name = 'site-faqs.html'
    context_object_name = 'faqs'
