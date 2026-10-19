import json
from src.models.league import League
from src.models.player import Player
from src.models.roster import Roster
from src.models.user import User
from src import config
import pprint

TEST_WEEK = 1

smackers_league = League.getSpecificLeagueById(config.SMACKERS_LEAGUE_ID)
# for u in smackers_league.getUsers():
#     print(u)



listRosters = smackers_league.getCurRosters()
# pprint.pprint(listRosters)
specRoster = Roster.getCurRosterFromLeague(1, listRosters)
print(f"roster id: {specRoster.roster_id}")
print(f"league id: {specRoster.league_id}")
print(f"week: {specRoster.week}")
print(f"starters: {specRoster.starter0}")

curPlayer = Player(specRoster.starter0)
print(f"player first name: {curPlayer.first_name}")
print(f"player last name: {curPlayer.last_name}")


# dictRosterIdtoUserId = {} # looks like { <roster_id>: User() }
# for r in listRosters:
#     dictRosterIdtoUserId[r["roster_id"]] = User(user_id=r["owner_id"], roster_id=r["roster_id"])

# for matchup in smackers_league.getMatchupsByWeek(TEST_WEEK):
#     curUser = dictRosterIdtoUserId[matchup["roster_id"]]
#     print(f"current user: {curUser.username}")
#     print(f"week {TEST_WEEK} score: {matchup['points']}")
#     for scorer in matchup["players_points"]:
#         curScorer = Player(scorer)
#         print(f"\t{curScorer} \t{matchup['players_points'][scorer]}")
#     print()

