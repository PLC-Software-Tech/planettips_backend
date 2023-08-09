from django.core.management.base import BaseCommand
from ...api_utils import fetch_teams

class Command(BaseCommand):
    help = 'Fetch teams from the API and create FootballTeam objects'

    def handle(self, *args, **kwargs):
        fetch_teams()
        self.stdout.write(self.style.SUCCESS('Teams fetched and created successfully!'))
