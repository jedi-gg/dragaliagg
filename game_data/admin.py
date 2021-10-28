from django.contrib import admin
from django.utils.html import format_html

from game_data.models import Adventurer, Wyrmprint, Dragon, Weapon


class ReadOnlyAdminMixin:
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Adventurer)
class AdventurerAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.get_image(size=120)))

    list_display = ['image_tag', 'name']

    search_fields = ['name']
    actions = None

@admin.register(Wyrmprint)
class WyrmprintAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.get_image(size=100)))

    list_display = ['image_tag', 'name', 'ability_name', 'ability_description']
    list_filter = ('rarity', 'affinity_name', )
    search_fields = ['name', 'ability_name']
    actions = None
    ordering = ('-rarity', 'name')


@admin.register(Dragon)
class DragonAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.get_image(size=100)))
    
    list_display = ['image_tag', 'name']

    search_fields = ['name']
    actions = None

@admin.register(Weapon)
class WeaponAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.get_image(size=60)))

    list_display = ['image_tag', 'name']
    search_fields = ['name']
    actions = None
