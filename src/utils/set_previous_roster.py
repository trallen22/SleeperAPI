import argparse
from src import config
import src.utils.database_utilities as db_utils
from src.models.player import Player
from src.models.league import League
import pprint


def get_args():
    """
    get_args: gets the command line arguments that were given 
    parameters: no parameters 
    returns: returns a dictionary of command line constants and their values 
    """
    parser = argparse.ArgumentParser(description='updates the matchup roster for a given rosterd id in a given week')
    # adding each argument to the parser 
    parser.add_argument('-d', '--DEBUG', action='store_true', help='log debug messages to LOGFILE')
    parser.add_argument('-e', '--EXECUTE', action='store_true', help="execute; overwrite and insert to database")
    parser.add_argument('-w', '--WEEK', required=True, help="delete old entries for the roster by week")
    parser.add_argument('-r', '--ROSTER', required=True, help="roster id")

    args, unknown = parser.parse_known_args()
    return vars(args) 

##############################
# Main Execution begins here 
##############################

argDict = get_args()
print(argDict)
week = argDict["WEEK"]
cur_roster_id = argDict["ROSTER"]
execute = argDict["EXECUTE"]

cur_league_id = config.SMACKERS_LEAGUE_ID_2026
smacker_league = League.getSpecificLeagueById(cur_league_id)

for m in smacker_league.getMatchupsByWeek(week):
    # pprint.pprint(m)
    if int(m.get("roster_id")) == int(cur_roster_id):
        cur_matchup_id = m["matchup_id"]
        break

starters = [
    "J.J. McCarthy",
    "Omarion Hampton",
    "Devin Singletary",
    "Zay Flowers",
    "Tee Higgins",
    "Antonio Williams",
    "Brock Bowers",
    "Tony Pollard",
    "Tyler Allgeier",
    "Tank Dell",
    
]
bench = [
    "Stetson Bennett",
    "Dillon Gabriel",
    "Haynes King",
    "Jalon Daniels",
    "Jameis Winston",
    "Tua Tagovailoa",
    "Malik Willis",
    "Andrei Iosivas",
    "Ja'Kobi Lane",
    "Ted Hurst",
    "Marquise Brown",
    "Rashod Bateman",
    "Marvin Mims",
    "Jalin Hyatt",
    "Eli Raridon",
    "Tommy Tremble",
    "Cade Otton",
]
reserve = [
    "Jeremiyah Love",
    "Alec Pierce"
]
taxi_squad = [
    "Pat Bryant",
    "Kyle Williams",
    "Jaylin Lane"
]

if execute:
    db_utils.sqlDelete(
        table=db_utils.MATCHUPS_TABLE,
        where={ "roster_id": cur_roster_id, "week": week }
    )


if execute:
    db_utils.sqlInsert(
        table=db_utils.MATCHUPS_TABLE,
        curTuple=(
            cur_matchup_id,
            cur_roster_id,
            cur_league_id,
            week,
            0, # TODO: could maybe get rid of total_points
            str([Player.getPlayerIdFromName(p) for p in starters]),
            str([Player.getPlayerIdFromName(b) for b in bench]),
            str([Player.getPlayerIdFromName(r) for r in reserve]),
            str([Player.getPlayerIdFromName(t) for t in taxi_squad])
        )
    )
