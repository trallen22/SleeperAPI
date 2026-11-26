import argparse
from app.core import config
import app.utils.database_utilities as db_utils
from app.models.player import Player
from app.models.league import League
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

def get_player_id_list(group: list[str]) -> list[str]:
    cur_id_list = []
    for p in group:
        if p[:3] == "ID:": # some players have the same name so use ID
            cur_id_list.append(p[3:])
        else:
            cur_id_list.append(Player.getPlayerIdFromName(p))
    return cur_id_list

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

cur_matchup_id = None
for m in smacker_league.getMatchupsByWeek(week, roster_id=cur_roster_id):
    # pprint.pprint(m)
    # print(f"roster_id: {m.get('roster_id')}")
    # print(f"cur roster id: {cur_roster_id}")
    if int(m.get("roster_id")) == int(cur_roster_id):
        pprint.pprint(m)
        cur_matchup_id = m["matchup_id"]
        break

if cur_matchup_id is None:
    print(f"ERROR: no matchup ID found for league='{smacker_league.league_id}' week='{week}' roster='{cur_roster_id}'")
    exit(1)

starters = [
    "Caleb Williams",
    "Rachaad White",
    "J'Mari Taylor",
    "Jordan Addison",
    "Wan'Dale Robinson",
    "Malik Washington",
    "Dallas Goedert",
    "Sam LaPorta",
    "ID:6794", # "Justin Jefferson",
    "Trevor Lawrence",
    "KC Concepcion",
    
]
bench = [
    "Drew Allar",
    "Quinn Ewers",
    "Anthony Richardson",
    "Cooper Rush",
    "Drew Lock",
    "Davis Mills",
    "Breece Hall",
    "Nicholas Singleton",
    "Kendre Miller",
    "Devin Neal",
    "Pierre Strong",
    "Brandon Aiyuk",
    "Mack Hollins",
    "Rashid Shaheed",
    "Luther Burden",
    "Colby Parkinson",
    "AJ Barner",
]
reserve = [
    "Michael Pittman",
]
taxi_squad = [
    "RJ Harvey",
    "Jalen Royals",
    "Jackson Hawes",
    
    "Brenen Thompson"
]

if execute:
    db_utils.sqlDelete(
        table=db_utils.MATCHUPS_TABLE,
        where={ "roster_id": cur_roster_id, "week": week }
    )

print(str(get_player_id_list(starters)))
print(str(get_player_id_list(bench)))
print(str(get_player_id_list(reserve)))
print(str(get_player_id_list(taxi_squad)))

if execute:
    db_utils.sqlInsert(
        table=db_utils.MATCHUPS_TABLE,
        curTuple=(
            cur_matchup_id,
            cur_roster_id,
            cur_league_id,
            week,
            0, # TODO: could maybe get rid of total_points
            str(get_player_id_list(starters)),
            str(get_player_id_list(bench)),
            str(get_player_id_list(reserve)),
            str(get_player_id_list(taxi_squad))
        )
    )
