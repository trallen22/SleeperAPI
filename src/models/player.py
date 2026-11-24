import json
from pathlib import Path
from src import config
import src.utils.database_utilities as db_utils

# path = "v1/players/nfl" # This is to get full player data; don't query more than once a day
BASE_DIR = Path(__file__).resolve().parent
PLAYERS_INFO_FILE = f"{BASE_DIR}/players.json"
playerInfoDict = None
try:
    with open(PLAYERS_INFO_FILE, 'r') as playerInfoFile:
        playerInfoDict = json.load(playerInfoFile)
except Exception as e:
    print(f"Error loading {PLAYERS_INFO_FILE}")
    print(f"ERROR:\n{e}")

class Player():
    def __init__(self, playerId: str):
        self.setPlayerInfo(playerId)
        self.weekly_points = {}

    def __str__(self):
        return str(self.full_name)

    def setPlayerInfo(self, playerId: str):
        try:
            curPlayer = playerInfoDict[str(playerId)]
        except KeyError:
            print(f"ERROR unable to find player with id: '{playerId}' in '{PLAYERS_INFO_FILE}'")
            curPlayer = dict()
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

    def getPointsByWeek(self, league_id: str, week: int):
        if not self.weekly_points.get(f"{week}"):
            points = db_utils.sqlSelect(
                table=db_utils.PLAYERS_POINTS_TABLE,
                where={ 'player_id': self.player_id, 'week': week, 'league_id': league_id },
                output="dict")
            print(f"POINTS: ")
            try:
                self.weekly_points = { f"{week}": points[0].get("points", None) }
            except IndexError:
                print(f"ERROR: no points found for week='{week}' and player='{self.player_id}' (name='{self.full_name}')")
                self.weekly_points = { f"{week}": "NA" }
        return self.weekly_points[f"{week}"]

    @classmethod
    def convertListOfIDs(cls, playerIds: str | list[int]):
        # make sure we have a list
        if isinstance(playerIds, str):
            playerIds = eval(playerIds)
        return [cls(pId) for pId in playerIds]

    @staticmethod
    def getPlayerIdFromName(player_name: str):
        playerId = None
        for p in playerInfoDict:
            if playerInfoDict[p].get("full_name") == player_name:
                playerId = p
                break
        if playerId is None:
            print(f"unable to find player id for '{player_name}'")
        return playerId

    # @staticmethod
    # def getPointsByWeekForList(listPlayerIds: list)

if __name__ == "__main__":
    testPlayer = Player(4943)
    print(testPlayer.full_name)
    # print(testPlayer.getPointsByWeek(config.SMACKERS_LEAGUE_ID_2026, 8))
    print(Player.getPlayerIdFromName(testPlayer.full_name))
    print(Player.getPlayerIdFromName("Pierre Strong"))
