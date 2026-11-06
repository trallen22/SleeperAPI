import argparse
from src.models.league import League
from src.models.roster import Roster
from src import config
import src.utils.database_utilities as db_utils
import pprint


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
cur_league_id = config.SMACKERS_LEAGUE_ID_2026

smackers_league = League.getSpecificLeagueById(cur_league_id)

listRosters = smackers_league.getCurRosters()

for matchup in smackers_league.getMatchupsByWeek(curWeek):
    print(f"MATCHUP: \n{pprint.pprint(matchup)}")
    curRoster = Roster.getCurRosterFromLeague(matchup["roster_id"], listRosters)

    print("matchup_id:")
    print(matchup['matchup_id'])
    print("roster_id:")
    print(matchup['roster_id'])
    print("league_id:")
    print(cur_league_id)
    print("week:")
    print(curWeek)
    print("points:")
    print(matchup['points'])
    print("starters:")
    print(f"{curRoster.starters}")
    # print(f"{matchup['starters']}")
    print("bench:")
    print(f"{curRoster.bench}")
    print("reserve:")
    print(f"{curRoster.reserve}")
    print("taxi:")
    print(f"{curRoster.taxi_squad}")
    print()

    if not dryRun:
        # Make sure this lines up with the matchups table schema
        exitCode = db_utils.sqlInsert(
            table=db_utils.MATCHUPS_TABLE,
            curTuple=(
                matchup['matchup_id'],
                matchup['roster_id'],
                cur_league_id,
                curWeek,
                matchup['points'],
                str(curRoster.starters),
                str(curRoster.bench),
                str(curRoster.reserve),
                str(curRoster.taxi_squad)
            )
        )
        if exitCode:
            print(f"failed to insert into {db_utils.MATCHUPS_TABLE} with exitCode {exitCode}")
    else:
        print("Running in dry-run mode; not updating table")
