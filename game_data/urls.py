from django.urls import path

from game_data.views import AdventurerDetail


urlpatterns = [
    path('<str:adventurer_slug>/', AdventurerDetail.as_view(), name='adventurer-detail'),
]
