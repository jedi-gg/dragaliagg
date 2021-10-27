from django.contrib import admin
from django.utils.html import format_html

from game_data.models import Adventurer, Wyrmprint, Dragon, Weapon


@admin.register(Adventurer)
class AdventurerAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Wyrmprint)
class WyrmprintAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.get_image(size=100)))

    list_display = ['image_tag', 'name', 'ability_name', 'ability_description']
    list_filter = ('rarity', 'affinity_name', )
    search_fields = ['name', 'ability_name']

@admin.register(Dragon)
class DragonAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    search_fields = ['name']
