from django.urls import path

from comps.views import Home


urlpatterns = [
    path('<str:slug>/', Home.as_view())
]
