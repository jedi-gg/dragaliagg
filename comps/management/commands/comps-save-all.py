from django.core.management.base import BaseCommand

from comps.models import Comp


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for c in Comp.objects.all():
            c.save()
