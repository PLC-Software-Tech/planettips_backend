from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime
from .models import *
from .serializers import *
from django.utils import timezone
from bs4 import BeautifulSoup
import requests
from django.db.models import Q

# Create your views here.

class MatchTipsView(generics.ListAPIView):
    queryset = MatchTips.objects.all().filter(
      Q(is_free=0) & Q(play_date__gte=datetime.today())
    ).select_related('home_team_id', 'away_team_id')
    serializer_class = MatchTipsSerializer



class MatchTipsHistoryView(generics.ListAPIView):
    queryset = MatchTips.objects.all().filter(
        Q(is_free=0) & Q(play_date__lt=datetime.today())
    ).select_related('home_team_id', 'away_team_id')
    serializer_class = MatchTipsSerializer
    # print(datetime.today())


class VIPTipsView(generics.ListAPIView):
    queryset = MatchTips.objects.filter(
        Q(is_free=1) & Q(play_date__gte=datetime.today())
        ).select_related('home_team_id', 'away_team_id')
    serializer_class = MatchTipsSerializer


class VIPTipsHistoryView(generics.ListAPIView):
    queryset = MatchTips.objects.all().filter(
             Q(is_free=1) & Q(play_date__lt=datetime.today())
    ).select_related('home_team_id', 'away_team_id')
    serializer_class = MatchTipsSerializer
    # print(datetime.today())


class CreateMatchTipsView(generics.CreateAPIView):
    queryset = MatchTips.objects.all()
    serializer_class = CreateMatchTipsSerializer


# class TopPredictionApi(generics.ListAPIView):
#     queryset = MatchTips.objects.all()
#     serializer_class = CreateMatchTipsSerializer
#     response = requests.get('https://www.livescore.com/en/')
#     soup = BeautifulSoup(response.text, 'lxml')
#     print(soup)

# class MatchTipsView(generics.ListCreateAPIView):
#     queryset = MatchTips.objects.all()
#     serializer_class = MatchTipsSerializer
