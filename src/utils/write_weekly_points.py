import argparse 
from src.models.league import League
from src import config
import src.utils.database_utilities as db_utils

def get_args():
    """
    get_args: gets the command line arguments that were given 
    parameters: no parameters 
    returns: returns a dictionary of command line constants and their values 
    """
    parser = argparse.ArgumentParser(description='generates a Trading Post')
    # adding each argument to the parser 
    parser.add_argument('-d', '--DEBUG', action='store_true', help='log debug messages to LOGFILE')
    parser.add_argument('-r', '--DRY-RUN', action='store_true', help="dry-run; don't insert to database") 

    args, unknown = parser.parse_known_args()
    return vars(args) 

##############################
# Main Execution begins here 
##############################

argDict = get_args()
print(argDict)
dryRun = argDict["DRY_RUN"]

curWeek = config.CUR_WEEK
curLeague = config.SMACKERS_LEAGUE_ID_2026

smackers_league = League.getSpecificLeagueById(curLeague)

for matchup in smackers_league.getMatchupsByWeek(curWeek):
    for p in matchup['players_points']:
        print(f"player: {p}\tpoints: {matchup['players_points'][p]}")
        if not dryRun:
            db_utils.sqlInsert(
                table=db_utils.PLAYERS_POINTS_TABLE, 
                curTuple=(
                    smackers_league.league_id, 
                    curWeek, 
                    p, 
                    matchup['players_points'][p]))
        else:
            print(f"Running in dry-run mode; database not uploaded")
