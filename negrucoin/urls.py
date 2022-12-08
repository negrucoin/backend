from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('penguin/', admin.site.urls),
    path('', include('main.urls')),
]
