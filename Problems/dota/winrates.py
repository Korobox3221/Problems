import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_hero_winrates(hero_name):
    url = f"https://www.dotabuff.com/heroes/{hero_name}/matchups"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve data for {hero_name}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'sortable'})

    if not table:
        print(f"No matchup data found for {hero_name}")
        return None

    rows = table.find_all('tr')
    winrates = []

    for row in rows[1:]:  # Skip the header row
        columns = row.find_all('td')
        if len(columns) < 3:
            continue

        versus_hero = columns[0].find('a').text.strip()
        winrate = columns[1].text.strip()
        matches_played = columns[2].text.strip()

        winrates.append({
            'Versus Hero': versus_hero,
            'Winrate': winrate,
            'Matches Played': matches_played
        })

    return winrates


def save_hero_winrates_to_csv(hero_name, winrates):
    if not winrates:
        print(f"No data to save for {hero_name}.")
        return

    df = pd.DataFrame(winrates)
    filename = f"{hero_name}_winrates.csv"
    df.to_csv(filename, index=False)
    print(f"Winrate data for {hero_name} saved to {filename}")


def scrape_and_save_winrates(hero_list):
    for hero_name in hero_list:
        print(f"Scraping winrate data for {hero_name}...")
        winrates = get_hero_winrates(hero_name)
        if winrates:
            save_hero_winrates_to_csv(hero_name, winrates)
        time.sleep(5)  # Add a delay to avoid overloading the server


def main():
    # Define your list of hero names (as per Dotabuff URL format)
    hero_list = [
        "natures-prophet",
        "lifestealer",
        "lone-druid",
        "dark-willow",
        "void-spirit",
        "pudge",
        "anti-mage",
        "crystal-maiden",
        "invoker",
        "juggernaut",
        "alchemist",
        "axe",
        "bristleback",
        "centaur-warrunner",
        "chaos-knight",
        "dawnbreaker",
        "bane",
        "bloodseeker",
        "earthshaker",
        "mirana",
        "shadow-fiend",
        "morphling",
        "phantom-lancer",
        "puck",
        "razor",
        "sand-king",
        "storm-spirit",
        "sven",
        "tiny",
        "vengeful-spirit",
        "windranger",
        "zeus",
        "kunkka",
        "lina",
        "lich",
        "lion",
        "shadow-shaman",
        "slardar",
        "tidehunter",
        "witch-doctor",
        "riki",
        "enigma",
        "tinker",
        "sniper",
        "necrolyte",
        "warlock",
        "beastmaster",
        "queen-of-pain",
        "venomancer",
        "faceless-void",
        "wraith-king",
        "death-prophet",
        "phantom-assassin",
        "pugna",
        "templar-assassin",
        "viper",
        "luna",
        "dragon-knight",
        "dazzle",
        "clockwerk",
        "leshrac",
        "dark-seer",
        "clinkz",
        "omniknight",
        "enchantress",
        "huskar",
        "night-stalker",
        "broodmother",
        "bounty-hunter",
        "weaver",
        "jakiro",
        "batrider",
        "chen",
        "spectre",
        "doom",
        "ancient-apparition",
        "ursa",
        "spirit-breaker",
        "gyrocopter",
        "silencer",
        "outworld-destroyer",
        "lycan",
        "brewmaster",
        "shadow-demon",
        "meepo",
        "treant-protector",
        "ogre-magi",
        "undying",
        "rubick",
        "disruptor",
        "nyx-assassin",
        "naga-siren",
        "keeper-of-the-light",
        "io",
        "visage",
        "slark",
        "medusa",
        "troll-warlord",
        "magnus",
        "timbersaw",
        "tusk",
        "skywrath-mage",
        "abaddon",
        "elder-titan",
        "legion-commander",
        "ember-spirit",
        "earth-spirit",
        "underlord",
        "terrorblade",
        "phoenix",
        "techies",
        "oracle",
        "winter-wyvern",
        "arc-warden",
        "monkey-king",
        "pangolier",
        "grimstroke",
        "hoodwink",
        "snapfire",
        "mars",
        "ringmaster",
        "marci",
        "primal-beast",
        "muerta"









    ]

    # Scrape and save winrate data for all heroes in the list
    scrape_and_save_winrates(hero_list)


if __name__ == "__main__":
    main()
