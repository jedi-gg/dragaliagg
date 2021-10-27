from django.urls import path

from comps.views import CompQuestList, CompSectionList, CompDetail


urlpatterns = [
    path('<str:section_slug>/<str:quest_slug>/<str:comp_slug>/', CompDetail.as_view(), name='comp-detail'),
    path('<str:section_slug>/<str:quest_slug>/', CompQuestList.as_view(), name='quest-list'),
    path('<str:section_slug>/', CompSectionList.as_view(), name='section-list'),
]
