from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from comps.enums import AdventurerSlotEnum
from core.models import SlugModel
from game_data.models import Adventurer, Dragon


class Comp(SlugModel):
    comp_type = models.ForeignKey('CompType', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    suffix = models.CharField(max_length=100, null=True, blank=True)
    creator = models.ForeignKey('CompCreator', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)
    auto_shapeshift = models.BooleanField(blank=True, null=True)
    game_version = models.CharField(max_length=100, blank=True, null=True)
    clear_time = models.CharField(max_length=50, blank=True, null=True)
    clear_rate = models.PositiveIntegerField(blank=True, null=True)
    clear_rate_note = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creators_notes = models.TextField(blank=True, null=True)
    discussion_link = models.URLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)

    section = models.ForeignKey('CompSection', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)
    quest = models.ForeignKey('CompQuest', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)
    difficulty = models.ForeignKey('CompDifficulty', related_name='comps', on_delete=models.DO_NOTHING, blank=True, null=True)

    shared_skill_1 = models.ForeignKey(Adventurer, related_name='comp_shared_skill_1', on_delete=models.DO_NOTHING, blank=True, null=True)
    shared_skill_2 = models.ForeignKey(Adventurer, related_name='comp_shared_skill_2', on_delete=models.DO_NOTHING, blank=True, null=True)

    helper = models.BooleanField(default=False)
    helper_dragon = models.ForeignKey(Dragon, related_name='helper', on_delete=models.DO_NOTHING, blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def slug_name(self):
        s = self
        return s.get_slug_string(
            s.post_date, s.difficulty, s.creator, s.suffix)
    
    def get_slug_string(self=None, date=None, difficulty=None, creator=None, suffix=None):
        slug_string = '{}-{}-{}'.format(
            date.strftime("%d%m%y"), difficulty, creator
        )

        if suffix:
            slug_string = '{}-{}'.format(slug_string, slugify(suffix))
        
        return slugify(slug_string)
    
    def get_team(self):
        comp_slots = {}
        for build in self.builds.all():
            comp_slots[build.slot] = build
        
        return comp_slots
    
    @property
    def get_title(self):
        suffix = ' {}'.format(self.suffix) if self.suffix else ''
        constructed_title = '{}: {} - {}{}'.format(
            self.quest, self.difficulty, self.creator, suffix)
        return self.title if self.title else constructed_title
    
    def get_lead(self):
        return self.builds.get(slot=AdventurerSlotEnum.LEAD_UNIT.value).adventurer
    
    def get_rest_of_team(self):
        rest_of_team = {}
        for build in self.builds.exclude(slot=AdventurerSlotEnum.LEAD_UNIT.value):
            rest_of_team[build.slot] = build.adventurer
        
        return rest_of_team
    
    def get_absolute_url(self):
        return reverse('comp-detail', kwargs={
            'comp_slug': self.slug,
            'section_slug': self.section.slug,
            'quest_slug': self.quest.slug,
            'difficulty_slug': self.difficulty.slug,
        })

    def __str__(self):
        return self.get_title
