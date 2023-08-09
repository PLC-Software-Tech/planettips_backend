from django.shortcuts import render
from rest_framework import generics
from .serializers import LeagueSerializer
from .models import Leagues
from .api_utils import *
from django.http import HttpResponse
from rest_framework.response import Response


# Create your views here.

class AllLeague(generics.ListAPIView):
    queryset = Leagues.objects.all()
    serializer_class = LeagueSerializer


class FetchDataAPIView(generics.ListCreateAPIView):
    queryset = Leagues.objects.all()
    serializer_class = LeagueSerializer

    def create(self, request, *args, **kwargs):
        fetch_and_store_data_from_api()
        return Response({'message': 'Data fetched and stored successfully!'})