"""
This file is for setting up the "league_rosters" table for the database
"""

from ..models import league
from .. import config
from .. import database_utilities as db_utils

def insert_league_rosters(league_id: int | str=None):
    """
    This function will insert league_id/roster_id/user_id from a specific league into the 'league_rosters' table
    """
    if league_id is None:
        print("ERROR: 'insert_users' requires a league_id")
        return 1
    smackers_league = league.League.getSpecificLeagueById(league_id)
    rosters = smackers_league.getCurRosters()
    for r in rosters:
        exitCode = db_utils.sqlInsert(db_utils.LEAGUE_ROSTERS_TABLE, (r.get('league_id'), r.get('roster_id'), r.get('owner_id')))
        if exitCode:
            print(f"ERROR: sqlInsert returned '{exitCode}'")
            return 1
    return 0

if __name__ == "__main__":
    insert_league_rosters(config.SMACKERS_LEAGUE_ID)