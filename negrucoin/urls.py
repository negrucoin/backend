from django.contrib import admin
from django.urls import path

from settings import API_PREFIX

urlpatterns = [
    path('penguin/', admin.site.urls),
    path(f'{API_PREFIX}/', lambda request: None),
]
