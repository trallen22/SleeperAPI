"""
This file is for setting up the "players" table for the database
"""

from src.models import player
from src import config
from src.utils import database_utilities as db_utils
import sys

def insert_players():
    """
    This function will insert player attributes from a player into the 'players' table
    """
    if player.playerInfoDict is None:
        print("ERROR: 'insert_players' requires playerInfoDict")
        return 1
    db_utils.sqlDelete(db_utils.PLAYERS_TABLE)
    for k, v in player.playerInfoDict.items():
        playerId = k
        firstName = v.get('first_name')
        lastName = v.get('last_name')
        fullName = v.get('full_name')
        stats_id = v.get('stats_id')
        college = v.get('college')
        position = v.get('position')
        fantasy_positions = v.get('fantasy_positions')
        if isinstance(fantasy_positions, list): # make sure list isn't null before .join()
            fantasy_positions = ",".join(fantasy_positions)
        team = v.get('team')
        team_abbr = v.get('team_abbr')

        exitCode = db_utils.sqlInsert(
            db_utils.PLAYERS_TABLE,
            (
                # must follow players-schema
                playerId,
                firstName,
                lastName,
                fullName,
                stats_id,
                college,
                position,
                fantasy_positions,
                team,
                team_abbr
            )
        )
        if exitCode:
            print(f"ERROR: sqlInsert returned '{exitCode}'")
            return 1
        # print("======")
        # print(k)
        # print(v.get('sport'))
        # print()
    return 0

if __name__ == "__main__":
    insert_players()