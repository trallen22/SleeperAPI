from src.models.league import League
from src.models.player import Player
from src.models.roster import Roster
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

def get_total_points_by_groups(league_id: str, roster_id: int, week: int, groups: list[str]=["starters", "bench"]) -> int:
    leagueMatchups = League.getSpecificLeagueById(leagueId=league_id).getMatchupsByWeek(week)
    # cur_roster = None
    # cur_starters = None
    all_groups = []
    for m in leagueMatchups:
        if (int(m['roster_id']) == int(roster_id)):
            # cur_roster = Roster(
                #     roster_id=roster_id,
                #     league_id=league_id,
                #     week=week,
                #     starters=m.get("starters"),
                #     bench=m.get("bench"),
                #     taxi=m.get("taxi"),
                #     reserve=m.get("reserve")
                # )
            for g in groups:
                # cur_starters = m.get(g)
                all_groups.extend(eval(m.get(g)))
            break

    starter_sql_query = db_utils.sqlSelect(
        table=db_utils.PLAYERS_POINTS_TABLE, 
        select=["SUM(points)"], 
        where={ 
            # "player_id": eval(cur_roster.starters),
            # "player_id": eval(cur_starters),
            "player_id": all_groups,
            "week": week,
            "league_id": league_id
        })
    # print(starter_sql_query)
    return starter_sql_query[0][0]

if __name__ == "__main__":
    TEST_LEAGUE = config.SMACKERS_LEAGUE_ID_2026
    TEST_ROSTER = 1
    TEST_WEEK = 6
    # print(get_player_week_points(config.SMACKERS_LEAGUE_ID_2026, 2, 10226))
    # print(Player(10226))
    print(get_total_points_by_groups(TEST_LEAGUE, roster_id=1, week=TEST_WEEK))