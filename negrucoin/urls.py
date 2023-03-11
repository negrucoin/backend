from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from main.views import TopPlayersView
from settings import API_PREFIX

urlpatterns = [
    path('penguin/', admin.site.urls, name='penguin'),
    path(f'{API_PREFIX}/top-players/', TopPlayersView.as_view(), name='top'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
