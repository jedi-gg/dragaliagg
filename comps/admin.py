from django import forms
from django.contrib import admin

from comps.forms import CompForm
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
        'dragon',
    ]

    raw_id_fields = (
        'weapon',
        'wyrmprint_1',
        'wyrmprint_2',
        'wyrmprint_3',
        'wyrmprint_4',
        'wyrmprint_5',
        'wyrmprint_6',
        'wyrmprint_7',
        'portrait_ability_slot_1',
        'portrait_ability_slot_2',
    )

    class Meta:
        widgets = {
            'wyrmprint_1': forms.TextInput(attrs={'size': 3}),
        }


@admin.register(Comp)
class CompAdmin(admin.ModelAdmin):
    form = CompForm
    inlines = [AdventurerBuildInline,]
    save_as = True
    save_on_top = True

    autocomplete_fields = [
        'creator',
        'shared_skill_1',
        'shared_skill_2',
        'section',
        'quest',
        'difficulty',
        'helper_dragon',
    ]

    raw_id_fields = (
        'parent_comp',
    )

    readonly_fields = ('slug',)

    search_fields = ['title', 'creator__name', 'slug']
    list_display = ['get_title', 'difficulty', 'creator', 'modified_date', 'created_date']
    list_filter = ('section', 'quest', 'difficulty',)

    def delete_model(self, request, object):
        # Manually delete adventurer builds
        for build in object.builds.all():
            build.delete()

        object.delete()

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