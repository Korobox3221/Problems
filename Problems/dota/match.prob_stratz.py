import os
import json
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import numpy as np
from scipy.special import expit  # Logistic function

# STRATZ API Key
STRATZ_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdWJqZWN0IjoiYmY2YTk0MDgtOTk2Ni00ZDQxLTk0MGYtNDc0Y2ZjYjVlODYzIiwiU3RlYW1JZCI6IjExMTAzNjIyNSIsIm5iZiI6MTczMTIwMDkzMiwiZXhwIjoxNzYyNzM2OTMyLCJpYXQiOjE3MzEyMDA5MzIsImlzcyI6Imh0dHBzOi8vYXBpLnN0cmF0ei5jb20ifQ.R5wAu7TZ0_J3vmJfcE7mx8sRkVXs87x6G_Voz1k_kQw"

# GraphQL Client Setup
transport = RequestsHTTPTransport(
    url="https://api.stratz.com/graphql",
    headers={"Authorization": f"Bearer {STRATZ_API_KEY}"},
    verify=True,
    retries=3,
)
client = Client(transport=transport, fetch_schema_from_transport=True)

# Cache directory


def fetch_hero_win_rates():
    """Fetch hero win rates from STRATZ."""
    query = gql("""
        {
            constants {
                heroes {
                    id
                    displayName
                    stats {
                        winRate
                    }
                }
            }
        }
    """)
    cache_file = os.path.join(CACHE_DIR, "hero_win_rates.json")
    data = fetch_data(query, cache_file)
    if data:
        heroes = data['constants']['heroes']
        return {hero['id']: hero['stats']['winRate'] for hero in heroes if hero['stats']}
    else:
        return {}


def fetch_hero_matchups(hero_id):
    """Fetch hero matchups (synergies and counters) from STRATZ."""
    query = gql(f"""
        {{
            heroStats {{
                matchup(heroId: {hero_id}) {{
                    heroId
                    winRate
                    matchCount
                }}
            }}
        }}
    """)
    cache_file = os.path.join(CACHE_DIR, f"hero_{hero_id}_matchups.json")
    data = fetch_data(query, cache_file)
    if data:
        return data['heroStats']['matchup']
    else:
        return []


def calculate_draft_score(team_picks, enemy_picks, hero_win_rates):
    """Calculate draft advantage based on hero win rates, synergies, and counters."""
    draft_score = 0

    # Add individual hero win rates
    for hero_id in team_picks:
        draft_score += hero_win_rates.get(hero_id, 0.5)  # Default to 50% if no data

    # Add synergies (heroes that work well together)
    for i in range(len(team_picks)):
        for j in range(i + 1, len(team_picks)):
            hero1 = team_picks[i]
            hero2 = team_picks[j]
            matchups1 = fetch_hero_matchups(hero1)
            matchups2 = fetch_hero_matchups(hero2)
            # Find synergy between hero1 and hero2
            for matchup in matchups1:
                if matchup['heroId'] == hero2:
                    draft_score += matchup['winRate'] / 100  # Convert percentage to decimal
            for matchup in matchups2:
                if matchup['heroId'] == hero1:
                    draft_score += matchup['winRate'] / 100  # Convert percentage to decimal

    # Subtract counters (enemy heroes that counter our picks)
    for hero_id in team_picks:
        for enemy_hero_id in enemy_picks:
            matchups = fetch_hero_matchups(hero_id)
            for matchup in matchups:
                if matchup['heroId'] == enemy_hero_id:
                    draft_score -= matchup['winRate'] / 100  # Convert percentage to decimal

    return draft_score


def win_probability(team_a, team_b, team_a_picks, team_b_picks, hero_win_rates):
    """Calculate win probability for Team A."""
    # Team strength (default to equal strength)
    team_strength_a = 0.5
    team_strength_b = 0.5

    # Draft advantage
    draft_score_a = calculate_draft_score(team_a_picks, team_b_picks, hero_win_rates)
    draft_score_b = calculate_draft_score(team_b_picks, team_a_picks, hero_win_rates)
    draft_advantage = draft_score_a - draft_score_b

    # Combine team strength and draft advantage
    combined_score = 0.6 * draft_advantage + 0.4 * (team_strength_a - team_strength_b) * 10
    return expit(combined_score)  # Logistic function


def main():
    # Fetch hero win rates
    hero_win_rates = fetch_hero_win_rates()

    # Input teams and hero picks
    team_a = input("Enter Team A name: ")
    team_b = input("Enter Team B name: ")
    team_a_picks = list(map(int, input("Enter Team A hero IDs (comma-separated): ").split(',')))
    team_b_picks = list(map(int, input("Enter Team B hero IDs (comma-separated): ").split(',')))

    # Calculate win probability
    prob = win_probability(team_a, team_b, team_a_picks, team_b_picks, hero_win_rates)
    print(f"{team_a} Win Probability: {prob * 100:.1f}%")


if __name__ == "__main__":
    main()
