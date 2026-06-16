"""
This file is for setting up the "users" table for the database
"""

from ..models import league
from ..models import user
from .. import config
from .. import database_utilities as db_utils

def insert_users(league_id: int | str=None):
    """
    This function will insert users from a specific league into the 'users' table
    """
    if league_id is None:
        print("ERROR: 'insert_users' requires a league_id")
        return 1
    smackers_league = league.League.getSpecificLeagueById(league_id)
    cur_users = smackers_league.getUsers()
    for u in cur_users:
        try:
            curID = u['user_id']
        except KeyError:
            print(f"ERROR: failed to get user_id for {u}")
            return 1
        foundUser = db_utils.sqlSelect(db_utils.USERS_TABLE, where={'user_id': curID})[0]
        if foundUser:
            print(f"INFO: found user ID '{foundUser[0]}' with username '{foundUser[1]}' in table '{db_utils.USERS_TABLE}'; skipping inserting into table")
            continue
        curUser = user.User(user_id=curID)
        exitCode = db_utils.sqlInsert(db_utils.USERS_TABLE, (curUser.user_id, curUser.username, curUser.display_name))
        if exitCode:
            print(f"ERROR: sqlInsert returned '{exitCode}'")
            return 1
    return 0

if __name__ == "__main__":
    insert_users(config.SMACKERS_LEAGUE_ID)