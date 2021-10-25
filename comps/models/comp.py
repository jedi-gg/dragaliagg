from django.db import models

from comps.enums import AdventurerSlotEnum
from core.models import SlugModel
from game_data.models import Adventurer


class Comp(SlugModel):
    comp_type = models.ForeignKey('CompType', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    creator = models.ForeignKey('CompCreator', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    auto_shapeshift = models.BooleanField(blank=True, null=True)
    game_version = models.CharField(max_length=100, blank=True, null=True)
    clear_time = models.CharField(max_length=50, blank=True, null=True)
    clear_rate = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creators_notes = models.TextField(blank=True, null=True)
    discussion_link = models.URLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)

    section = models.ForeignKey('CompSection', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)
    quest = models.ForeignKey('CompQuest', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)
    difficulty = models.ForeignKey('CompDifficulty', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)

    shared_skill_1 = models.ForeignKey(Adventurer, related_name='comp_shared_skill_1', on_delete=models.DO_NOTHING, blank=True, null=True)
    shared_skill_2 = models.ForeignKey(Adventurer, related_name='comp_shared_skill_2', on_delete=models.DO_NOTHING, blank=True, null=True)

    def slug_name(self):
        return self.title
    
    def get_team(self):
        comp_slots = {}
        for build in self.builds.all():
            comp_slots[build.slot] = build.adventurer
        
        return comp_slots
    
    def get_lead(self):
        return self.builds.get(slot=AdventurerSlotEnum.LEAD_UNIT.value).adventurer
    
    def get_rest_of_team(self):
        rest_of_team = {}
        for build in self.builds.exclude(slot=AdventurerSlotEnum.LEAD_UNIT.value):
            rest_of_team[build.slot] = build.adventurer
        
        return rest_of_team

    def __str__(self):
        return self.title
