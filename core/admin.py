from django.contrib import admin

from core.models import SiteFAQ


@admin.register(SiteFAQ)
class SiteFAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'order_weight',]

    search_fields = ['question']
    ordering = ('-order_weight', 'question')
