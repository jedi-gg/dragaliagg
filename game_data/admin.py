from django.contrib import admin

from game_data.models import Adventurer, Wyrmprint, Dragon, Weapon


@admin.register(Adventurer)
class AdventurerAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Wyrmprint)
class WyrmprintAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Dragon)
class DragonAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    search_fields = ['name']