from django.urls import path

from comps.views import CompDetail, CompList


urlpatterns = [
    path('<str:section_slug>/<str:quest_slug>/<str:difficulty_slug>/<int:pk>-<str:comp_slug>/', CompDetail.as_view(), name='comp-detail'),
    path('<str:section_slug>/<str:quest_slug>/<str:difficulty_slug>/', CompList.as_view(), name='comp-list'),
    path('<str:section_slug>/<str:quest_slug>/', CompList.as_view(), name='comp-list'),
    path('<str:section_slug>/', CompList.as_view(), name='comp-list'),
]
