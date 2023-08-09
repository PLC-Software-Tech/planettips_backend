from django.db import models


# Create your models here.

class Leagues(models.Model):
    idLeague = models.CharField(max_length=255,null=True)
    strLeague = models.CharField(max_length=255,null=True)
    strSport = models.CharField(max_length=255,null=True)
    strLeagueAlternate = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.idLeague
