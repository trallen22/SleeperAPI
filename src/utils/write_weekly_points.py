from src.models.league import League
from src import config
import src.utils.database_utilities as db_utils

# curWeek = config.CUR_WEEK
curWeek = 7
curLeague = config.SMACKERS_LEAGUE_ID_2026

smackers_league = League.getSpecificLeagueById(curLeague)

for matchup in smackers_league.getMatchupsByWeek(curWeek):
    for p in matchup['players_points']:
        print(f"player: {p}\tpoints: {matchup['players_points'][p]}")
        db_utils.sqlInsert(
            table=db_utils.PLAYERS_POINTS_TABLE, 
            curTuple=(
                smackers_league.league_id, 
                curWeek, 
                p, 
                matchup['players_points'][p]))
