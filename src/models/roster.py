from league import League
import database_utilities as db_utils

class Roster():
    def __init__(self, roster_id: str, league_id: str, week: str, starters: list=None, bench: list=None):
        self.roster_id = roster_id
        self.league_id = league_id
        self.week = week
        for s in range(len(starters)):
            setattr(self, )
        self.bench = None

    @classmethod
    def getSpecificRosterByWeek(cls, roster_id: str, league_id: str, week: str|int) -> "Roster":
        pass

    

if __name__ == "__main__":

    SMACKERS_LEAGUE_ID = "1259602742452690944" # Lexington Smackers
    TEST_WEEK = 1
    smackers_league = League.getSpecificLeagueById(SMACKERS_LEAGUE_ID)
    matchups = smackers_league.getMatchupsByWeek(TEST_WEEK)
    print(matchups)