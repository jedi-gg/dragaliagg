from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from comps.views import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adventurer/', include('game_data.urls')),
    path('', include('comps.urls')),
    path('', Home.as_view(), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
