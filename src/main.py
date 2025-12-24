import json
from league import League
from player import Player
from user import User

USERNAME = "tallen21"
USER_ID = "839972291348639744"
SMACKERS_LEAGUE_ID = "1259602742452690944" # Lexington Smackers
SMACKERS_USERS = [
    "LongJohnSilvers23",
    "blakespencer18",
    "RKozemko193",
    "SoupOrMan53",
    "JasonGarcia12",
    "Astaton24",
    "Bean216",
    "Jallen2202",
    "Braceandrew8",
    "Cbranham",
    "jackiebaseball",
    "tallen21"
]

TEST_WEEK = 1

smackers_league = League.getSpecificLeagueById(SMACKERS_LEAGUE_ID)
listRosters = smackers_league.getCurRosters()
dictRosterIdtoUserId = {} # looks like { <roster_id>: User() }
for r in listRosters:
    dictRosterIdtoUserId[r["roster_id"]] = User(user_id=r["owner_id"], roster_id=r["roster_id"])

for matchup in smackers_league.getMatchupsByWeek(TEST_WEEK):
    curUser = dictRosterIdtoUserId[matchup["roster_id"]]
    print(f"current user: {curUser.username}")
    print(f"week {TEST_WEEK} score: {matchup['points']}")
    for scorer in matchup["players_points"]:
        curScorer = Player(scorer)
        print(f"\t{curScorer} \t{matchup['players_points'][scorer]}")
    print()