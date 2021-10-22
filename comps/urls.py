from django.urls import path

from comps.views import CompQuestList, CompSectionList


urlpatterns = [
    path('<str:section_slug>/<str:quest_slug>/', CompQuestList.as_view(), name='quest-list'),
    path('<str:section_slug>/', CompSectionList.as_view(), name='section-list'),
]
