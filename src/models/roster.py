

class roster():
    def __init__(self):
        self.roster_id = None
        self.year_week = None
        self.starters = None
        self.bench = None

if __name__ == "__main__":
    from models.league import League

    SMACKERS_LEAGUE_ID = "1259602742452690944" # Lexington Smackers
    TEST_WEEK = 1
    smackers_league = League.getSpecificLeagueById(SMACKERS_LEAGUE_ID)
    matchups = smackers_league.getMatchupsByWeek(TEST_WEEK)
    print(matchups)