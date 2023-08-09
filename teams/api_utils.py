import requests
from .models import *
from league.models import Leagues


def fetch_teams():
    # api_url = 'https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l=French%20Ligue%201'
    
    myLeagues = Leagues.objects.filter(strSport='Soccer')
    for myLeague in myLeagues:
        league_name=myLeague.strLeague.replace(' ','%20')

        api_url = f'https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l={league_name}'
        
        response = requests.get(url=api_url)
        all_teams = response.json()
        # print(all_teams)
        if all_teams['teams'] != 'None':
          for team in all_teams['teams']:
            FootballTeam.objects.get_or_create(
            idTeam=team['idTeam'],
            idSoccerXML=team['idSoccerXML'],
            idAPIfootball=team['idAPIfootball'],
            intLoved=team['intLoved'],
            strTeam=team['strTeam'],
            strTeamShort=team['strTeamShort'],
            strAlternate=team['strAlternate'],
            intFormedYear=team['intFormedYear'],
            strSport=team['strSport'],
            strLeague=team['strLeague'],
            idLeague=team['idLeague'],
            strLeague2=team['strLeague2'],
            idLeague2=team['idLeague2'],
            strLeague3=team['strLeague3'],
            idLeague3=team['idLeague3'],
            strLeague4=team['strLeague4'],
            idLeague4=team['idLeague4'],
            strLeague5=team['strLeague5'],
            idLeague5=team['idLeague5'],
            strLeague6=team['strLeague6'],
            idLeague6=team['idLeague6'],
            strLeague7=team['strLeague7'],
            idLeague7=team['idLeague7'],
            strDivision=team['strDivision'],
            strStadium=team['strStadium'],
            strKeywords=team['strKeywords'],
            strRSS=team['strRSS'],
            strStadiumThumb=team['strStadiumThumb'],
            strStadiumDescription=team['strStadiumDescription'],
            strStadiumLocation=team['strStadiumLocation'],
            intStadiumCapacity=team['intStadiumCapacity'],
            strWebsite=team['strWebsite'],
            strFacebook=team['strFacebook'],
            strTwitter=team['strTwitter'],
            strInstagram=team['strInstagram'],
            strDescriptionEN=team['strDescriptionEN'],
            strDescriptionDE=team['strDescriptionDE'],
            strDescriptionFR=team['strDescriptionFR'],
            strDescriptionCN=team['strDescriptionCN'],
            strDescriptionIT=team['strDescriptionIT'],
            strDescriptionJP=team['strDescriptionJP'],
            strDescriptionRU=team['strDescriptionRU'],
            strDescriptionES=team['strDescriptionES'],
            strDescriptionPT=team['strDescriptionPT'],
            strDescriptionSE=team['strDescriptionSE'],
            strDescriptionNL=team['strDescriptionNL'],
            strDescriptionHU=team['strDescriptionHU'],
            strDescriptionNO=team['strDescriptionNO'],
            strDescriptionIL=team['strDescriptionIL'],
            strDescriptionPL=team['strDescriptionPL'],
            strKitColour1=team['strKitColour1'],
            strKitColour2=team['strKitColour2'],
            strKitColour3=team['strKitColour3'],
            strGender=team['strGender'],
            strCountry=team['strCountry'],
            strTeamBadge=team['strTeamBadge'],
            strTeamJersey=team['strTeamJersey'],
            strTeamLogo=team['strTeamLogo'],
            strTeamFanart1=team['strTeamFanart1'],
            strTeamFanart2=team['strTeamFanart2'],
            strTeamFanart3=team['strTeamFanart3'],
            strTeamFanart4=team['strTeamFanart4'],
            strTeamBanner=team['strTeamBanner'],
            strYoutube=team['strYoutube'],
            strLocked=team['strLocked']
        )

    


    
    
    
