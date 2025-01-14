import requests
from django.core.management.base import BaseCommand
from evaluations.models import Player
import time


class Command(BaseCommand):
    help = "Fetch NBA player data from Sportradar API"

    API_KEY = 'GWJo7ee4kITPWy2Q1ov4Qf0x1Vc2kSrfIlQpjAp0'
    TEAM_URL = 'https://api.sportradar.us/nba/trial/v8/en/league/teams.json'
    TEAM_PROFILE_URL = 'https://api.sportradar.us/nba/trial/v8/en/teams/{team_id}/profile.json'
    PLAYER_PROFILE_URL = 'https://api.sportradar.us/nba/trial/v8/en/players/{player_id}/profile.json'

    def fetch_api_data(self, url, retries=5):
        headers = {"accept": "application/json"}
        for attempt in range(retries):
            response = requests.get(url, headers=headers)
            
            if response.status_code == 429:  # Rate limit error
                retry_after = int(response.headers.get("Retry-After", 1))  # Fallback to 1 second
                print(f"Rate limit reached. Retrying after {retry_after} seconds... (Attempt {attempt + 1}/{retries})")
                time.sleep(retry_after)
                continue  # Retry the request

            if response.status_code == 200:
                return response.json()  # Successful response

            response.raise_for_status()  # Raise other errors
        print(f"Failed to fetch data after {retries} attempts. URL: {url}")
        return None  # Return None if all retries fail


    def fetch_teams(self):
        url = f"{self.TEAM_URL}?api_key={self.API_KEY}"
        print(f"Fetching teams from URL: {url}")
        data = self.fetch_api_data(url)
        teams = data.get("teams", [])
        return teams

    def fetch_team_roster(self, team_id):
        url = self.TEAM_PROFILE_URL.format(team_id=team_id) + f"?api_key={self.API_KEY}"
        print(f"Fetching roster for team ID: {team_id}")
        data = self.fetch_api_data(url)
        return data.get("players", [])

    def fetch_player_profile(self, player_id):
        url = self.PLAYER_PROFILE_URL.format(player_id=player_id) + f"?api_key={self.API_KEY}"
        print(f"Fetching profile for player ID: {player_id}")
        return self.fetch_api_data(url)

    def handle(self, *args, **kwargs):
        teams = self.fetch_teams()
        for team in teams:
            print(f"Fetching roster for {team['name']}...")
            roster = self.fetch_team_roster(team['id'])

            for player in roster:
                print(f"Fetching profile for {player['full_name']}...")
                profile = self.fetch_player_profile(player['id'])

                if not profile:
                    print(f"Failed to fetch profile for player ID: {player['id']}")
                    continue

                # Handle statistics and averages
                stats = profile.get('statistics', {})
                stats_average = stats.get('average', {})

                if not stats_average:
                    print(f"Missing stats for player {player['full_name']} (ID: {player['id']})")
                    stats_average = {}

                # Save Player Data
                Player.objects.update_or_create(
                    id=player['id'],  # UUID from the API
                    defaults={
                        'name': player.get('full_name', 'Unknown'),
                        'position': player.get('primary_position', 'Unknown'),
                        'height': player.get('height', 'N/A'),
                        'weight': player.get('weight', 'N/A'),

                        # Stats from averages
                        'points_per_game': stats_average.get('points', 0.0),
                        'rebounds_per_game': stats_average.get('rebounds', 0.0),
                        'assists_per_game': stats_average.get('assists', 0.0),
                        'steals_per_game': stats_average.get('steals', 0.0),
                        'blocks_per_game': stats_average.get('blocks', 0.0),
                        'turnovers_per_game': stats_average.get('turnovers', 0.0),
                        'field_goal_percentage': stats_average.get('field_goals_pct', 0.0),
                        'three_point_percentage': stats_average.get('three_points_pct', 0.0),
                        'free_throw_percentage': stats_average.get('free_throws_pct', 0.0),
                        'efficiency_rating': stats_average.get('efficiency', 0.0),
                        'true_shooting_percentage': stats_average.get('true_shooting_pct', 0.0),
                        'usage_percentage': stats_average.get('usage_pct', 0.0),
                    }
                )

                # Debugging: Confirm save
                print(f"Saved player {player['full_name']} with Points/Game: {stats_average.get('points', 0.0)}, Rebounds/Game: {stats_average.get('rebounds', 0.0)}")
                time.sleep(1)  # QPS compliance
            time.sleep(1)  # Avoid rate limits between teams


