from django.db import models

from game_data.models import Adventurer


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

    # adventurer_1 = models.ForeignKey(AdventurerBuild, related_name='comp_adventurer_1', on_delete=models.DO_NOTHING, blank=True, null=True)
    # adventurer_2 = models.ForeignKey(AdventurerBuild, related_name='comp_adventurer_2', on_delete=models.DO_NOTHING, blank=True, null=True)
    # adventurer_3 = models.ForeignKey(AdventurerBuild, related_name='comp_adventurer_3', on_delete=models.DO_NOTHING, blank=True, null=True)
    # adventurer_4 = models.ForeignKey(AdventurerBuild, related_name='comp_adventurer_4', on_delete=models.DO_NOTHING, blank=True, null=True)
