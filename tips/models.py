from django.db import models
from teams.models import FootballTeam


# Create your models here.


class MatchTips(models.Model):
    home_team_id = models.ForeignKey(FootballTeam, on_delete=models.CASCADE, related_name='home_team')
    away_team_id = models.ForeignKey(FootballTeam, on_delete=models.CASCADE, related_name='away_team')
    match_tips = models.TextField(max_length=255, null=True)
    result = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    is_free = models.IntegerField(default=0)
    play_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)


class TopPrediction(models.Model):
    league_name = models.CharField(max_length=255, null=True, blank=True)
    league_short_name = models.CharField(max_length=255, null=True, blank=True)
    league_icon = models.CharField(max_length=255, null=True)
    home_team = models.CharField(max_length=255, null=True, blank=True)
    away_team = models.CharField(max_length=255, null=True, blank=True)
    home_team_probability = models.IntegerField(null=True, blank=True)
    away_team_probability = models.IntegerField(null=True)
    draw_probability = models.IntegerField(null=True)
    prediction = models.CharField(max_length=255, null=True)
    correct_score = models.CharField(max_length=255, null=True)
    avg_goals = models.CharField(max_length=255, null=True)
    odds = models.CharField(max_length=255, null=True)
    live_odds = models.CharField(max_length=255, null=True)
    score = models.CharField(max_length=255, null=True)
    play_date = models.CharField(max_length=255, null=True)
