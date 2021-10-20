from django.contrib import admin

from comps.models import Comp, AdventurerBuild


class AdventurerBuildInline(admin.StackedInline):
    model = AdventurerBuild
    extra = 4

    autocomplete_fields = [
        'adventurer',
        'adventurer_wp_1',
        'adventurer_wp_2',
        'adventurer_wp_3',
        'adventurer_wp_4',
        'adventurer_wp_5',
        'adventurer_wp_6',
        'adventurer_wp_7',
        'adventurer_dragon',
        'adventurer_weapon',
    ]

@admin.register(Comp)
class CompAdmin(admin.ModelAdmin):
    inlines = [AdventurerBuildInline,]
    autocomplete_fields = [
        'shared_skill_1',
        'shared_skill_2',
    ]
