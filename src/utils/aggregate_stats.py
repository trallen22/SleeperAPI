from src.models.player import Player
import src.utils.database_utilities as db_utils
from src import config

def get_player_week_points(league_id: str, week: int, player_id: int):
    pointsSQLquery = db_utils.sqlSelect(
        table=db_utils.PLAYERS_POINTS_TABLE, 
        where={ 
            "league_id": league_id,
            "week": week,
            "player_id": player_id
        }
    )
    if len(pointsSQLquery) == 0: # we didn't find it in the db
        print(f"did not find any points for league_id: '{league_id}', week: '{week}', and player_id: '{player_id}' in {db_utils.PLAYERS_POINTS_TABLE}")
    return pointsSQLquery

if __name__ == "__main__":
    print(get_player_week_points(config.SMACKERS_LEAGUE_ID_2026, 2, 10226))
    print(Player(10226))