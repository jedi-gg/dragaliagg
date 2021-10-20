from django.contrib import admin

from comps.models import Comp


@admin.register(Comp)
class CompAdmin(admin.ModelAdmin):
    autocomplete_fields = [
        'shared_skill_1',
        'shared_skill_2',
        'adventurer_1',
        'adventurer_1_wp_1',
        'adventurer_1_wp_2',
        'adventurer_1_wp_3',
        'adventurer_1_wp_4',
        'adventurer_1_wp_5',
        'adventurer_1_wp_6',
        'adventurer_1_wp_7',
        'adventurer_1_dragon',
        'adventurer_1_weapon',
    ]
