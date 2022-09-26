from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework import status

from main.forms import LoginForm, RegistrationForm
from main.models import Client


class IndexView(TemplateView):
    """Simple index page view."""
    template_name = 'main/index.html'


class LoginView(View):
    """Login view. Uses LoginForm."""

    def get(self, request) -> HttpResponse:
        """Get rendered form LoginForm."""
        next_page = request.GET.get('next', '/')
        form = LoginForm(request.POST or None)
        context = {
            'form': form,
            'next': next_page
        }
        return render(request, 'main/login.html', context)

    def post(self, request) -> HttpResponse:
        """Post entered user data."""
        next_page = request.GET.get('next', '/')
        form = LoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(next_page)

        context = {
            'form': form,
            'next': next_page
        }
        return render(request, 'main/login.html', context, status=status.HTTP_401_UNAUTHORIZED)


class RegistrationView(View):
    """Registration view. Uses RegistrationForm form."""

    def get(self, request) -> HttpResponse:
        """Get rendered form."""
        next_page = request.GET.get('next', '/')
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form,
            'next': next_page
        }
        return render(request, 'main/registration.html', context)

    def post(self, request) -> HttpResponse:
        """Post form data."""
        next_page = request.GET.get('next', '/')
        form = RegistrationForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create base User
            new_user = form.save(commit=False)
            new_user.username = username
            new_user.save()
            new_user.set_password(password)
            new_user.save()

            # Create our model Client
            Client.objects.create(
                user=new_user
            )

            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(next_page)

        context = {
            'form': form,
            'next': next_page
        }
        return render(
            request,
            'main/registration.html',
            context,
            status=status.HTTP_401_UNAUTHORIZED
        )
