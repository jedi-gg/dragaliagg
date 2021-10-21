from django.conf import settings

from comps.models import CompSection

def nav_items(request):
    return {
        'sections': CompSection.objects.all().order_by('ordering')
    }
