from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from .api_utils import *


# Create your views here.

class Teams(generics.ListCreateAPIView):
    queryset = FootballTeam.objects.all()
    serializer_class = TeamSerializer
    
    def create(self, request, *args, **kwargs):
        fetch_teams()
        return Response({'message': 'Data fetched and stored successfully!'})


