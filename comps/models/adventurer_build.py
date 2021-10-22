from django.db import models

from game_data.models import Adventurer, Wyrmprint, Dragon, Weapon
from comps.enums import AdventurerSlotEnum
from comps.models import Comp

class AdventurerBuild(models.Model):
    comp = models.ForeignKey(Comp, related_name='builds', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer = models.ForeignKey(Adventurer, related_name='builds', on_delete=models.DO_NOTHING, blank=True, null=True)
    slot = models.PositiveSmallIntegerField(choices=AdventurerSlotEnum.as_tuples(), default=AdventurerSlotEnum.LEAD_UNIT.value)
    adventurer_wp_1 = models.ForeignKey(Wyrmprint, related_name='comp_build_adventurer_wp_1', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_2 = models.ForeignKey(Wyrmprint, related_name='comp_build_adventurer_wp_2', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_3 = models.ForeignKey(Wyrmprint, related_name='comp_build_adventurer_wp_3', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_4 = models.ForeignKey(Wyrmprint, related_name='comp_build_adventurer_wp_4', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_5 = models.ForeignKey(Wyrmprint, related_name='comp_build_adventurer_wp_5', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_6 = models.ForeignKey(Wyrmprint, related_name='comp_build_adventurer_wp_6', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_7 = models.ForeignKey(Wyrmprint, related_name='comp_build_adventurer_wp_7', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_dragon = models.ForeignKey(Dragon, related_name='comp_build_dragon', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_weapon = models.ForeignKey(Weapon, related_name='comp_build_weapon', on_delete=models.DO_NOTHING, blank=True, null=True)
