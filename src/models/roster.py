from src.models import sleeper_api
from src.models.league import League
from src.utils import database_utilities as db_utils
from src import config

class Roster():
    def __init__(self, roster_id: str, league_id: str, week: str, starters: list=None, bench: list=None, taxi: list=None, reserve: list=None):
        self.roster_id = roster_id
        self.league_id = league_id
        self.week = week
        # This seems redundant
        self.starters = starters
        self.bench = bench
        self.taxi_squad = taxi
        self.reserve = reserve
        for s in range(len(starters)):
            setattr(self, f'starter{s}', starters[s])
        # self.bench = None

    @classmethod
    def getSpecificRosterByWeek(cls, roster_id: str, league_id: str, week: str|int) -> "Roster":
        pass

    @classmethod
    def getCurRosterFromLeague(cls, roster_id: str, all_rosters: list[dict]) -> "Roster":
        for r in all_rosters:
            if r['roster_id'] == roster_id:
                curStarters = r['starters']
                nonStarters = [p for p in r['players'] if p not in set(curStarters)]
                curTaxi = r.get('taxi')
                if curTaxi is None:
                    curTaxi = []
                curBench = [p for p in nonStarters if p not in set(curTaxi)]
                return Roster(roster_id=roster_id, league_id=r['league_id'], week=99, starters=curStarters, bench=curBench, taxi=r.get('taxi'), reserve=r.get('reserve'))

if __name__ == "__main__":
    TEST_WEEK = 1
    smackers_league = League.getSpecificLeagueById(config.SMACKERS_LEAGUE_ID_2026)
    matchups = smackers_league.getMatchupsByWeek(TEST_WEEK)
    print(matchups)