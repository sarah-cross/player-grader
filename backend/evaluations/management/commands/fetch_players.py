import requests
from django.core.management.base import BaseCommand
from evaluations.models import Player
import time


class Command(BaseCommand):
    help = "Fetch NBA player data from Sportradar API"

    API_KEY = 'BSnCDaQ7teJvfpTKIQBUphyxVbi5imOnE2j2RpdI'
    TEAM_URL = 'https://api.sportradar.us/nba/trial/v8/en/league/teams.json'
    TEAM_PROFILE_URL = 'https://api.sportradar.us/nba/trial/v8/en/teams/{team_id}/profile.json'
    PLAYER_PROFILE_URL = 'https://api.sportradar.us/nba/trial/v8/en/players/{player_id}/profile.json'

    NBA_TEAM_IDS = {
        "583ec87d-fb46-11e1-82cb-f4ce4684ea4c",  # 76ers
        "583ec5fd-fb46-11e1-82cb-f4ce4684ea4c",  # Bulls
        "583ec773-fb46-11e1-82cb-f4ce4684ea4c",  # Cavaliers
        "583eccfa-fb46-11e1-82cb-f4ce4684ea4c",  # Celtics
        "583ecdfb-fb46-11e1-82cb-f4ce4684ea4c",  # Clippers
        "583ecefd-fb46-11e1-82cb-f4ce4684ea4c",  # Bucks
        "583eca88-fb46-11e1-82cb-f4ce4684ea4c",  # Grizzlies
        "583ecb8f-fb46-11e1-82cb-f4ce4684ea4c",  # Hawks
        "583ecea6-fb46-11e1-82cb-f4ce4684ea4c",  # Heat
        "583ec97e-fb46-11e1-82cb-f4ce4684ea4c",  # Hornets
        "583ece50-fb46-11e1-82cb-f4ce4684ea4c",  # Jazz
        "583ed0ac-fb46-11e1-82cb-f4ce4684ea4c",  # Kings
        "583ec70e-fb46-11e1-82cb-f4ce4684ea4c",  # Knicks
        "583ecae2-fb46-11e1-82cb-f4ce4684ea4c",  # Lakers
        "583ed157-fb46-11e1-82cb-f4ce4684ea4c",  # Magic
        "583ecf50-fb46-11e1-82cb-f4ce4684ea4c",  # Mavericks
        "583ec9d6-fb46-11e1-82cb-f4ce4684ea4c",  # Nets
        "583ed102-fb46-11e1-82cb-f4ce4684ea4c",  # Nuggets
        "583ec7cd-fb46-11e1-82cb-f4ce4684ea4c",  # Pacers
        "583ecc9a-fb46-11e1-82cb-f4ce4684ea4c",  # Pelicans
        "583ec928-fb46-11e1-82cb-f4ce4684ea4c",  # Pistons
        "583ecda6-fb46-11e1-82cb-f4ce4684ea4c",  # Raptors
        "583ecb3a-fb46-11e1-82cb-f4ce4684ea4c",  # Rockets
        "583ecd4f-fb46-11e1-82cb-f4ce4684ea4c",  # Spurs
        "583ecfa8-fb46-11e1-82cb-f4ce4684ea4c",  # Suns
        "583ecfff-fb46-11e1-82cb-f4ce4684ea4c",  # Thunder
        "583eca2f-fb46-11e1-82cb-f4ce4684ea4c",  # Timberwolves
        "583ed056-fb46-11e1-82cb-f4ce4684ea4c",  # Trail Blazers
        "583ec825-fb46-11e1-82cb-f4ce4684ea4c",  # Warriors
        "583ec8d4-fb46-11e1-82cb-f4ce4684ea4c",  # Wizards
    }


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
        all_teams = data.get("teams", [])

        # Filter for NBA teams
        nba_teams = [team for team in all_teams if team["id"] in self.NBA_TEAM_IDS]
        print(f"Fetched {len(nba_teams)} NBA teams")
        return nba_teams

    def fetch_team_roster(self, team_id):
        url = self.TEAM_PROFILE_URL.format(team_id=team_id) + f"?api_key={self.API_KEY}"
        print(f"Fetching roster for team ID: {team_id}")
        data = self.fetch_api_data(url)
        return data.get("players", [])

    def fetch_player_profile(self, player_id):
        url = self.PLAYER_PROFILE_URL.format(player_id=player_id) + f"?api_key={self.API_KEY}"
        print(f"Fetching profile for player ID: {player_id}")
        response = self.fetch_api_data(url)

        if not response:
            print(f"No data returned for player ID: {player_id}")
            return None

        # Extract player profile details
        profile = {
            'id': response.get('id'),
            'full_name': response.get('full_name', 'Unknown'),
            'position': response.get('primary_position', 'Unknown'),
            'height': response.get('height', 'N/A'),
            'weight': response.get('weight', 'N/A'),
            'team': response.get('team', {}).get('name', 'Unknown'),
        }

        # Find the most recent regular season stats
        seasons = response.get('seasons', [])
        for season in sorted(seasons, key=lambda s: s['year'], reverse=True):
            if season['type'] == 'REG':
                team_data = season['teams'][0]  # Assuming single team per season
                profile['statistics'] = team_data.get('average', {})
                break
        else:
            print(f"No regular season data found for player ID: {player_id}")
            profile['statistics'] = {}

        return profile


    def handle(self, *args, **kwargs):
        teams = self.fetch_teams()
        for team in teams:
            self.stdout.write(f"Fetching roster for {team['name']}...")
            roster = self.fetch_team_roster(team['id'])

            for player in roster:
                self.stdout.write(f"Fetching profile for {player['full_name']}...")
                profile = self.fetch_player_profile(player['id'])

                if not profile or 'statistics' not in profile:
                    print(f"Failed to fetch profile or stats for player ID: {player['id']}")
                    continue

                stats = profile['statistics']

                # Update or create the Player object
                Player.objects.update_or_create(
                    id=profile['id'],  # UUID from the API
                    defaults={
                        'name': profile['full_name'],
                        'position': profile['position'],
                        'height': profile['height'],
                        'weight': profile['weight'],
                        'team': profile['team'],

                        # Statistics
                        'points_per_game': stats.get('points', 0.0),
                        'rebounds_per_game': stats.get('rebounds', 0.0),
                        'assists_per_game': stats.get('assists', 0.0),
                        'steals_per_game': stats.get('steals', 0.0),
                        'blocks_per_game': stats.get('blocks', 0.0),
                        'turnovers_per_game': stats.get('turnovers', 0.0),
                        'field_goals_made': stats.get('field_goals_made', 0.0),
                        'field_goals_att': stats.get('field_goals_att', 0.0),
                        'three_points_made': stats.get('three_points_made', 0.0),
                        'three_points_att': stats.get('three_points_att', 0.0),
                        'free_throws_made': stats.get('free_throws_made', 0.0),
                        'free_throws_att': stats.get('free_throws_att', 0.0),
                        'efficiency': stats.get('efficiency', 0.0),
                    }
                )

                # Debugging: Print saved player
                print(f"Saved player {profile['full_name']} with stats: {stats}")
            time.sleep(1)  # Avoid rate limits



