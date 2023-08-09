from rest_framework import serializers
from .models import *
from teams.serializers import *


class MatchTipsSerializer(serializers.ModelSerializer):
    home_team_id = TeamSerializer()
    away_team_id = TeamSerializer()

    class Meta:
        model = MatchTips
        fields = '__all__'


class CreateMatchTipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchTips
        fields = '__all__'

