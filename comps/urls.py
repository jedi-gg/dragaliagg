from django.urls import path

from comps.views import CompQuestDetail, CompSectionDetail


urlpatterns = [
    path('<str:section_slug>/<str:quest_slug>/', CompQuestDetail.as_view()),
    path('<str:section_slug>/', CompSectionDetail.as_view()),
]
