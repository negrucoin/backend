from django.contrib.auth.views import LogoutView
from django.urls import path

from main.views import IndexView, RegistrationView, LoginView, GetMoneyCountView
from settings import API_PREFIX

urlpatterns = [
    path(f'{API_PREFIX}/get-money-count', GetMoneyCountView.as_view(), name='money-count'),

    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('sign-in/', RegistrationView.as_view(), name='sign-in'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
