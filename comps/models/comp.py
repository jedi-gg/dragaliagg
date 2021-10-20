from django.db import models

from game_data.models import Adventurer, Wyrmprint, Dragon, Weapon


class Comp(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    game_version = models.CharField(max_length=100)
    clear_time = models.CharField(max_length=50)
    clear_rate = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    discussion_link = models.URLField()
    video_link = models.URLField()

    shared_skill_1 = models.ForeignKey(Adventurer, related_name='comp_shared_skill_1', on_delete=models.DO_NOTHING, blank=True, null=True)
    shared_skill_2 = models.ForeignKey(Adventurer, related_name='comp_shared_skill_2', on_delete=models.DO_NOTHING, blank=True, null=True)

    # Adventurer 1
    adventurer_1 = models.ForeignKey(Adventurer, related_name='comp_adventurer_1', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_1 = models.ForeignKey(Wyrmprint, related_name='comp_adventurer_1_wp_1', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_2 = models.ForeignKey(Wyrmprint, related_name='comp_adventurer_1_wp_2', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_3 = models.ForeignKey(Wyrmprint, related_name='comp_adventurer_1_wp_3', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_4 = models.ForeignKey(Wyrmprint, related_name='comp_adventurer_1_wp_4', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_5 = models.ForeignKey(Wyrmprint, related_name='comp_adventurer_1_wp_5', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_6 = models.ForeignKey(Wyrmprint, related_name='comp_adventurer_1_wp_6', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_wp_7 = models.ForeignKey(Wyrmprint, related_name='comp_adventurer_1_wp_7', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_1_dragon = models.ForeignKey(Dragon, related_name='comp_dragon_1', on_delete=models.DO_NOTHING, blank=True, null=True)
    adventurer_1_weapon = models.ForeignKey(Weapon, related_name='comp_weapon_1', on_delete=models.DO_NOTHING, blank=True, null=True)
