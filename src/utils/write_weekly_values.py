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
    # TODO: actually add this
    parser.add_argument('-d', '--DEBUG', action='store_true', help='log debug messages to LOGFILE')
    parser.add_argument('-e', '--EXECUTE', action='store_true', help="execute and insert to database") 

    args, unknown = parser.parse_known_args()
    return vars(args) 

# TODO: actually implement returning something
def write_weekly_points(cur_week: int, cur_league_id: str, execute: bool) -> int:
    smackers_league = League.getSpecificLeagueById(cur_league_id)

    for matchup in smackers_league.getMatchupsByWeek(cur_week):
        for p in matchup['players_points']:
            print(f"player: {p}\tpoints: {matchup['players_points'][p]}")
            if execute:
                db_utils.sqlInsert(
                    table=db_utils.PLAYERS_POINTS_TABLE, 
                    curTuple=(
                        smackers_league.league_id, 
                        cur_week, 
                        p, 
                        matchup['players_points'][p]))
            else:
                print(f"Running in dry-run mode; database not uploaded")

# TODO: actually implement returning something
def write_weekly_rosters(cur_week: int, cur_league_id: str, execute: bool=False) -> int:
    smackers_league = League.getSpecificLeagueById(cur_league_id)

    listRosters = smackers_league.getCurRosters()

    for matchup in smackers_league.getMatchupsByWeek(cur_week):
        print(f"MATCHUP: \n{pprint.pprint(matchup)}")
        curRoster = Roster.getCurRosterFromLeague(matchup["roster_id"], listRosters)

        print("matchup_id:")
        print(matchup['matchup_id'])
        print("roster_id:")
        print(matchup['roster_id'])
        print("league_id:")
        print(cur_league_id)
        print("week:")
        print(cur_week)
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

        if execute:
            # Make sure this lines up with the matchups table schema
            exitCode = db_utils.sqlInsert(
                table=db_utils.MATCHUPS_TABLE,
                curTuple=(
                    matchup['matchup_id'],
                    matchup['roster_id'],
                    cur_league_id,
                    cur_week,
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

##############################
# Main Execution begins here 
##############################

if __name__ == "__main__":
    argDict = get_args()
    print(argDict)
    execute: bool = argDict["EXECUTE"]

    curWeek = config.CUR_WEEK
    curLeague = config.SMACKERS_LEAGUE_ID_2026

    write_weekly_rosters(cur_week=curWeek, cur_league_id=curLeague, execute=execute)
