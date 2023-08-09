from django.db import models

# Create your models here.
from django.db import models


class FootballTeam(models.Model):
    idTeam = models.CharField(max_length=10, null=True)
    idSoccerXML = models.CharField(max_length=10, null=True)
    idAPIfootball = models.CharField(max_length=10, null=True)
    intLoved = models.CharField(max_length=5,null=True)
    strTeam = models.CharField(max_length=255, null=True)
    strTeamShort = models.CharField(max_length=10, null=True)
    strAlternate = models.TextField(blank=True, null=True)
    intFormedYear = models.CharField(max_length=4, null=True)
    strSport = models.CharField(max_length=100, null=True)
    strLeague = models.CharField(max_length=100, null=True)
    idLeague = models.CharField(max_length=10, null=True)
    strLeague2 = models.CharField(max_length=100, null=True)
    idLeague2 = models.CharField(max_length=10, null=True)
    strLeague3 = models.CharField(max_length=100, null=True)
    idLeague3 = models.CharField(max_length=10, null=True)
    strLeague4 = models.CharField(max_length=100, null=True)
    idLeague4 = models.CharField(max_length=10, null=True)
    strLeague5 = models.CharField(max_length=100, blank=True, null=True)
    idLeague5 = models.CharField(max_length=10, blank=True, null=True)
    strLeague6 = models.CharField(max_length=100, blank=True, null=True)
    idLeague6 = models.CharField(max_length=10, blank=True, null=True)
    strLeague7 = models.CharField(max_length=100, blank=True, null=True)
    idLeague7 = models.CharField(max_length=10, blank=True, null=True)
    strDivision = models.CharField(max_length=100, blank=True, null=True)
    strStadium = models.CharField(max_length=255, null=True)
    strKeywords = models.CharField(max_length=255, null=True)
    strRSS = models.URLField(blank=True, null=True)
    strStadiumThumb = models.URLField(blank=True, null=True)
    strStadiumDescription = models.TextField(blank=True, null=True)
    strStadiumLocation = models.CharField(max_length=255, blank=True, null=True)
    intStadiumCapacity = models.IntegerField(blank=True, null=True)
    strWebsite = models.URLField(blank=True, null=True)
    strFacebook = models.URLField(blank=True, null=True)
    strTwitter = models.URLField(blank=True, null=True)
    strInstagram = models.URLField(blank=True, null=True)
    strDescriptionEN = models.TextField(blank=True, null=True)
    strDescriptionDE = models.TextField(blank=True, null=True)
    strDescriptionFR = models.TextField(blank=True, null=True)
    strDescriptionCN = models.TextField(blank=True, null=True)
    strDescriptionIT = models.TextField(blank=True, null=True)
    strDescriptionJP = models.TextField(blank=True, null=True)
    strDescriptionRU = models.TextField(blank=True, null=True)
    strDescriptionES = models.TextField(blank=True, null=True)
    strDescriptionPT = models.TextField(blank=True, null=True)
    strDescriptionSE = models.TextField(blank=True, null=True)
    strDescriptionNL = models.TextField(blank=True, null=True)
    strDescriptionHU = models.TextField(blank=True, null=True)
    strDescriptionNO = models.TextField(blank=True, null=True)
    strDescriptionIL = models.TextField(blank=True, null=True)
    strDescriptionPL = models.TextField(blank=True, null=True)
    strKitColour1 = models.CharField(max_length=7, blank=True, null=True)
    strKitColour2 = models.CharField(max_length=7, blank=True, null=True)
    strKitColour3 = models.CharField(max_length=7, blank=True, null=True)
    strGender = models.CharField(max_length=10, blank=True, null=True)
    strCountry = models.CharField(max_length=100, blank=True, null=True)
    strTeamBadge = models.URLField(blank=True, null=True)
    strTeamJersey = models.URLField(blank=True, null=True)
    strTeamLogo = models.URLField(blank=True, null=True)
    strTeamFanart1 = models.URLField(blank=True, null=True)
    strTeamFanart2 = models.URLField(blank=True, null=True)
    strTeamFanart3 = models.URLField(blank=True, null=True)
    strTeamFanart4 = models.URLField(blank=True, null=True)
    strTeamBanner = models.URLField(blank=True, null=True)
    strYoutube = models.URLField(blank=True, null=True)
    strLocked = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.strTeam