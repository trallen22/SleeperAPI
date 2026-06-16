import json
from models.league import League
from models.player import Player
from models.user import User
import config

TEST_WEEK = 1

smackers_league = League.getSpecificLeagueById(config.SMACKERS_LEAGUE_ID)
for u in smackers_league.getUsers():
    print(u)



# listRosters = smackers_league.getCurRosters()
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

