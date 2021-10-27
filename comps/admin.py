from django import forms
from django.contrib import admin

from comps.models import (
    Comp,
    CompSection,
    CompQuest,
    CompDifficulty,
    AdventurerBuild,
    CompCreator,
    CompType,
)


class AdventurerBuildInline(admin.StackedInline):
    model = AdventurerBuild
    extra = 4

    autocomplete_fields = [
        'adventurer',
        'adventurer_dragon',
        'adventurer_weapon',
    ]

    raw_id_fields = (
        'adventurer_wp_1',
        'adventurer_wp_2',
        'adventurer_wp_3',
        'adventurer_wp_4',
        'adventurer_wp_5',
        'adventurer_wp_6',
        'adventurer_wp_7',
    )

    class Meta:
        widgets = {
            'adventurer_wp_1': forms.TextInput(attrs={'size': 3}),
        }


@admin.register(Comp)
class CompAdmin(admin.ModelAdmin):
    inlines = [AdventurerBuildInline,]
    save_as = True

    autocomplete_fields = [
        'creator',
        'shared_skill_1',
        'shared_skill_2',
        'section',
        'quest',
        'difficulty',
    ]

@admin.register(CompSection)
class CompSectionAdmin(admin.ModelAdmin):
    search_fields = ['title',]
    save_as = True


@admin.register(CompQuest)
class CompQuestAdmin(admin.ModelAdmin):
    save_as = True
    search_fields = ['title',]
    autocomplete_fields = [
        'section',
    ]

@admin.register(CompDifficulty)
class CompDifficultyAdmin(admin.ModelAdmin):
    search_fields = ['title',]

@admin.register(CompType)
class CompTypeAdmin(admin.ModelAdmin):
    search_fields = ['name',]

@admin.register(CompCreator)
class CompCreatorAdmin(admin.ModelAdmin):
    search_fields = ['name',]