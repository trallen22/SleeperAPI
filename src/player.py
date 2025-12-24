import json
from base_sleeper_api import BaseSleeperAPI

# path = "v1/players/nfl" # This is to get full player data; don't query more than once a day
PLAYERS_INFO_FILE = "players.json"
try:
    with open(PLAYERS_INFO_FILE, 'r') as playerInfoFile:
        playerInfoDict = json.load(playerInfoFile)
except Exception as e:
    print(f"Error loading {PLAYERS_INFO_FILE}")
    print(f"ERROR:\n{e}")

class Player(BaseSleeperAPI):
    def __init__(self, playerId: str):
        self.setPlayerInfo(playerId)

    def __str__(self):
        return self.full_name

    def setPlayerInfo(self, playerId: str):
        try:
            curPlayer = playerInfoDict[str(playerId)]
        except KeyError:
            print(f"ERROR unable to find player with id: '{playerId}' in '{PLAYERS_INFO_FILE}'")
            return
        self.fantasy_positions = curPlayer.get("fantasy_positions")
        self.last_name = curPlayer.get("last_name")
        self.first_name = curPlayer.get("first_name")
        self.full_name = curPlayer.get("full_name")
        self.player_id = curPlayer.get("player_id")
        self.college = curPlayer.get("college")
        self.stats_id = curPlayer.get("stats_id")
        self.position = curPlayer.get("position")
        self.team = curPlayer.get("team")
        self.team_abbr = curPlayer.get("team_abbr")

if __name__ == "__main__":
    testPlayer = Player(3992)
    print(testPlayer.full_name)