from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from main.forms import LoginForm, RegistrationForm
from main.models import Client
from main.serializers import MoneyCountSerializer, TopPlayersSerializer
from main.services.money_service import MoneyService
from main.services.top_service import TopService


class GetMoneyCountView(APIView):
    """View that called every 10 sec on a client to update him balance."""

    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        client = request.user.client
        money_count = MoneyService.get_client_money_count(client)
        return Response(MoneyCountSerializer(money_count).data)


class TopPlayersView(APIView):
     def get(self, _: Request, count: int = 3) -> Response:
        service = TopService()
        top_players = service.get_top_players(count=count)
        return Response(TopPlayersSerializer(top_players).data)
