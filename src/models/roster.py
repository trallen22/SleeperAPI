from src.models import sleeper_api
from src.models.league import League
from src.utils import database_utilities as db_utils

class Roster():
    def __init__(self, roster_id: str, league_id: str, week: str, starters: list=None, bench: list=None):
        self.roster_id = roster_id
        self.league_id = league_id
        self.week = week
        for s in range(len(starters)):
            setattr(self, f'starter{s}', starters[s])
        self.bench = None

    @classmethod
    def getSpecificRosterByWeek(cls, roster_id: str, league_id: str, week: str|int) -> "Roster":
        pass

    @classmethod
    def getCurRosterFromLeague(cls, roster_id: str, all_rosters: list[dict]) -> "Roster":
        for r in all_rosters:
            if r['roster_id'] == roster_id:
                return Roster(roster_id=roster_id, league_id=r['league_id'], week=99, starters=r['starters'])

if __name__ == "__main__":

    SMACKERS_LEAGUE_ID = "1259602742452690944" # Lexington Smackers
    TEST_WEEK = 1
    smackers_league = League.getSpecificLeagueById(SMACKERS_LEAGUE_ID)
    matchups = smackers_league.getMatchupsByWeek(TEST_WEEK)
    print(matchups)