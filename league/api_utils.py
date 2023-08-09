import requests
from .models import Leagues


def fetch_and_store_data_from_api():
    api_url = "https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"  # Replace with the actual API endpoint

    try:
        response = requests.get(api_url)
        data = response.json()

        for league_data in data['leagues']:
            id_league = league_data['idLeague']
            str_league = league_data['strLeague']
            strSport = league_data['strSport']
            str_league_alternate = league_data['strLeagueAlternate']

            # Check if the league already exists, update if needed, or create a new entry
            league, created = Leagues.objects.get_or_create(
                idLeague=id_league,
                defaults={'strLeague': str_league,'strSport':strSport, 'strLeagueAlternate': str_league_alternate}
            )

    except requests.exceptions.RequestException as e:
        # Handle API request errors
        print("Error fetching data:", e)
