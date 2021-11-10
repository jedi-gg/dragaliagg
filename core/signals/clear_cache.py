from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from comps.models import Comp, CompSection, CompQuest

@receiver(post_save, sender=Comp)
@receiver(post_save, sender=CompSection)
@receiver(post_save, sender=CompQuest)
def clear_cache(sender, instance, **kwargs):
    cache.clear()
