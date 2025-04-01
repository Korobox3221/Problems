import csv
import lane_lists
import numpy as np
from scipy.special import expit

from lane_lists import hero_data

team_a = [
        'morphling_winrates.csv',  #pos 1, index = 0
        'pangolier_winrates.csv', #pos 2, index = 1
        'timbersaw_winrates.csv', #pos 3, index = 2
        'lion_winrates.csv', #pos 4, index = 3
        'warlock_winrates.csv' #pos 5, index = 4
    ]

team_b = [
        'phantom-assassin_winrates.csv', #pos 1, index = 0
        'tiny_winrates.csv', #pos 2, index = 1
        'lycan_winrates.csv', #pos 3, index = 2
        'tusk_winrates.csv', #pos 4, index = 3
        'phoenix_winrates.csv' #pos 5, index = 4
    ]

META_DATA = lane_lists.meta
META_DATA_1 = lane_lists.meta_1
META_DATA_2 = lane_lists.meta_2
META_DATA_3 = lane_lists.meta_3
META_DATA_4 = lane_lists.meta_4
META_DATA_5 = lane_lists.meta_5
def get_hero_winrate(hero):
    """Get the base win rate of a hero."""
    return META_DATA.get(hero, {}).get('winrate', 0.5)

def get_hero_tier(hero):
    """Get the meta tier of a hero."""
    return META_DATA.get(hero, {}).get('tier', 'C')
def get_hero_winrate_0(hero):
    """Get the base win rate of a hero."""
    return META_DATA_1.get(hero, {}).get('winrate', 0.5)

def get_hero_tier_0(hero):
    """Get the meta tier of a hero."""
    return META_DATA_1.get(hero, {}).get('tier', 'C')

def get_hero_winrate_1(hero):
    """Get the base win rate of a hero."""
    return META_DATA_2.get(hero, {}).get('winrate', 0.5)

def get_hero_tier_1(hero):
    """Get the meta tier of a hero."""
    return META_DATA_2.get(hero, {}).get('tier', 'C')

def get_hero_winrate_2(hero):
    """Get the base win rate of a hero."""
    return META_DATA_3.get(hero, {}).get('winrate', 0.5)

def get_hero_tier_2(hero):
    """Get the meta tier of a hero."""
    return META_DATA_3.get(hero, {}).get('tier', 'C')

def get_hero_winrate_3(hero):
    """Get the base win rate of a hero."""
    return META_DATA_4.get(hero, {}).get('winrate', 0.5)

def get_hero_tier_3(hero):
    """Get the meta tier of a hero."""
    return META_DATA_4.get(hero, {}).get('tier', 'C')


def get_hero_winrate_4(hero):
    """Get the base win rate of a hero."""
    return META_DATA_5.get(hero, {}).get('winrate', 0.5)

def get_hero_tier_4(hero):
    """Get the meta tier of a hero."""
    return META_DATA_5.get(hero, {}).get('tier', 'C')

def calculate_lane_advantage(team_lane):
    """Calculate the advantage for a lane based on hero matchups and meta tiers."""
    advantage = 0
    pos1_tier = get_hero_tier_0(team_lane[0].replace('_winrates.csv', '').replace('-', ' ').title())
    pos2_tier = get_hero_tier_1(team_lane[1].replace('_winrates.csv', '').replace('-', ' ').title())
    pos3_tier = get_hero_tier_2(team_lane[2].replace('_winrates.csv', '').replace('-', ' ').title())
    pos4_tier = get_hero_tier_3(team_lane[3].replace('_winrates.csv', '').replace('-', ' ').title())
    pos5_tier = get_hero_tier_4(team_lane[4].replace('_winrates.csv', '').replace('-', ' ').title())

    positions_tiers = [pos1_tier, pos2_tier, pos3_tier, pos4_tier, pos5_tier]

    pos1_winrate = get_hero_winrate_0(team_lane[0].replace('_winrates.csv', '').replace('-', ' ').title())
    pos2_winrate = get_hero_winrate_1(team_lane[1].replace('_winrates.csv', '').replace('-', ' ').title())
    pos3_winrate = get_hero_winrate_2(team_lane[2].replace('_winrates.csv', '').replace('-', ' ').title())
    pos4_winrate = get_hero_winrate_3(team_lane[3].replace('_winrates.csv', '').replace('-', ' ').title())
    pos5_winrate = get_hero_winrate_4(team_lane[4].replace('_winrates.csv', '').replace('-', ' ').title())

    positions_winrates = [pos1_winrate, pos2_winrate, pos3_winrate, pos4_winrate, pos5_winrate]

    for i in range(5):
        winrate = positions_winrates[i]
        tier = positions_tiers[i]
        if tier == 'S':
            advantage += 0.05
        elif tier == 'A':
            advantage += 0.03
        elif tier == 'B':
            advantage += 0.01
        # Base win rate contribution
        advantage += (winrate- 0.5) * 0.2


    return advantage
def load_matchups(filename):
    matchups = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hero = row['Winrate']
            winrate = float(row['Matches Played'].strip('%'))
            matchups[hero] = winrate
    return matchups

percent_sum = 0
for hero in team_a:
    for enemy in range(len(team_b)):
        matchup = load_matchups(hero)[team_b[enemy].replace('_winrates.csv', '').replace('-', ' ').title()]
        print(f"{hero.replace('_winrates.csv', '').replace('-', ' ').title()} has {matchup}% against {team_b[enemy].replace('_winrates.csv', '').replace('-', ' ').title()}")
        percent_sum += matchup
print('All hero matchups:',percent_sum)
pos1_vs_pos4 = load_matchups(team_a[0])[team_b[3].replace('_winrates.csv', '').replace('-', ' ').title()]
pos1_vs_pos3 = load_matchups(team_a[0])[team_b[2].replace('_winrates.csv', '').replace('-', ' ').title()]
pos5_vs_pos4 = load_matchups(team_a[4])[team_b[3].replace('_winrates.csv', '').replace('-', ' ').title()]
pos5_vs_pos3 = load_matchups(team_a[4])[team_b[2].replace('_winrates.csv', '').replace('-', ' ').title()]
pos2_vs_pos2 = load_matchups(team_a[1])[team_b[1].replace('_winrates.csv', '').replace('-', ' ').title()]
pos4_vs_pos5 = load_matchups(team_a[3])[team_b[4].replace('_winrates.csv', '').replace('-', ' ').title()]
pos4_vs_pos1 =  load_matchups(team_a[3])[team_b[0].replace('_winrates.csv', '').replace('-', ' ').title()]
pos3_vs_pos5 = load_matchups(team_a[2])[team_b[4].replace('_winrates.csv', '').replace('-', ' ').title()]
pos3_vs_pos1 = load_matchups(team_a[2])[team_b[0].replace('_winrates.csv', '').replace('-', ' ').title()]
safe_lane = (pos5_vs_pos3 + pos1_vs_pos3 + pos1_vs_pos4 + pos5_vs_pos4)
hard_lane = (pos3_vs_pos1 + pos3_vs_pos5 + pos4_vs_pos1 + pos4_vs_pos5)
mid_lane = pos2_vs_pos2 * 2
meta_team_a = calculate_lane_advantage(team_a)*100
meta_team_b = calculate_lane_advantage(team_b)*100
meta_diff = meta_team_a - meta_team_b
print("Meta team A:",meta_team_a)
print("Meta team B:",meta_team_b)
print("Safe lane diff:",safe_lane)
print("Mid lane diff:",mid_lane)
print("Hard lane diff:",hard_lane)
print("Meta diff",round(meta_diff))
if meta_diff<0:
    percent_sum += safe_lane + hard_lane + mid_lane + abs(meta_diff)
else:
    percent_sum += safe_lane + hard_lane + mid_lane - meta_diff
if percent_sum<0:
    print(f"Your team has ADVANTAGE +{round(abs(percent_sum))}%")
else:
    print(f"Your team has DISADVANTAGE -{round(percent_sum)}%")
