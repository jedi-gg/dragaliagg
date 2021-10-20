from django.contrib import admin
from django.urls import path

from comps.views import Home


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', Home.as_view(), name='home'),

]
