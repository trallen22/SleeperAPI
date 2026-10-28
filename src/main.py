import json
from src.models.league import League
from src.models.player import Player
from src.models.roster import Roster
from src.models.user import User
from src import config
import pprint

TEST_WEEK = 5

smackers_league = League.getSpecificLeagueById(config.SMACKERS_LEAGUE_ID_2026)
# for u in smackers_league.getUsers():
#     print(u)


listRosters = smackers_league.getCurRosters()
# pprint.pprint(listRosters)
specRoster = Roster.getCurRosterFromLeague(1, listRosters)
# print(f"roster id: {specRoster.roster_id}")
# print(f"league id: {specRoster.league_id}")
# print(f"week: {specRoster.week}")
# # print(f"starters: {specRoster.starter0}")
print(f"starters: {specRoster.starters}")
print(f"bench: {specRoster.bench}")
print(f"taxi: {specRoster.taxi_squad}")
print(type(specRoster.starters))

# for p in specRoster.taxi_squad:
#     curPlayer = Player(p)
#     print(f"cur player id: {curPlayer.player_id}")
#     print(f"player first name: {curPlayer.first_name}")
#     print(f"player last name: {curPlayer.last_name}")


# dictRosterIdtoUserId = {} # looks like { <roster_id>: User() }
# for r in listRosters:
#     dictRosterIdtoUserId[r["roster_id"]] = User(user_id=r["owner_id"], roster_id=r["roster_id"])

# for matchup in smackers_league.getMatchupsByWeek(TEST_WEEK):
    # print(f"MATCHUP: \n{pprint.pprint(matchup)}")
    # curUser = dictRosterIdtoUserId[matchup["roster_id"]]
    # curRoster = Roster.getCurRosterFromLeague(matchup["roster_id"], listRosters)
    # # pprint.pprint(matchup)
    # print(f"current user: {curUser.username}")
    # print(f"week {TEST_WEEK} score: {matchup['points']}")
    # # separate starters and bench
    # curStarters = matchup["starters"]
    # curBench = [p for p in matchup["players"] if p not in (set(curStarters) | set(curRoster.taxi_squad))]

    # print("starters:")
    # for scorer in curStarters:
    #     curScorer = Player(scorer)
    #     print(f"\t{curScorer} \t{matchup['players_points'][scorer]}")
    # print("bench:")
    # for benchScorer in curBench:
    #     curScorer = Player(benchScorer)
    #     print(f"\t{curScorer} \t{matchup['players_points'][benchScorer]}")
    # print("taxi:")
    # for curTaxi in curRoster.taxi_squad:
    #     curScorer = Player(curTaxi)
    #     print(f"\t{curScorer} \t{matchup['players_points'][curTaxi]}")
    # print()

