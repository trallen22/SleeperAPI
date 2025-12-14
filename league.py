from base_sleeper_api import BaseSleeperAPI

class League(BaseSleeperAPI):
    SPORT = "nfl"
    SEASON = "2025"

    def __init__(self, leagueInfo: dict):
        self.name = leagueInfo.get("name")
        self.league_id = leagueInfo.get("league_id")
        self.total_rosters = leagueInfo.get("total_rosters")
        self.status = leagueInfo.get("status")
        self.sport = leagueInfo.get("sport")
        self.settings = leagueInfo.get("settings")
        self.season_type = leagueInfo.get("season_type")
        self.season = leagueInfo.get("season") 
        self.scoring_settings = leagueInfo.get("scoring_settings")
        self.roster_positions = leagueInfo.get("roster_positions")
        self.previous_league_id = leagueInfo.get("previous_league_id")
        self.draft_id = leagueInfo.get("draft_id")
        self.avatar = leagueInfo.get("avatar")

    # class methods
    @classmethod
    def _apiGetSpecificLeagueById(cls, leagueId: str) -> list[dict]:
        return super().callApi(f"v1/league/{leagueId}")

    @classmethod
    def getSpecificLeagueById(cls, leagueId: str) -> str:
        league = League(cls._apiGetSpecificLeagueById(leagueId))
        return league

    # instance methods
    def getRosters(self) -> list:
        roster = self._apiGetRostersByLeagueId(self.league_id)
        return roster

    def getUsers(self) -> list[dict]:
        listUsers = self._apiGetUsersByLeagueId()
        return listUsers

    def getMatchupsByWeek(self, week: int) -> list[dict]:
        matchups = self._apiGetMatchupsByWeekByLeagueId(week)
        return matchups

    # private instance methods
    def _apiGetRostersByLeagueId(self) -> list[dict]:
        return super().callApi(f"v1/league/{self.league_id}/rosters")

    def _apiGetUsersByLeagueId(self) -> list[dict]:
        return super().callApi(f"v1/league/{self.league_id}/users")

    def _apiGetMatchupsByWeekByLeagueId(self, week: int) -> list[dict]:
        return super().callApi(f"v1/league/{self.league_id}/matchups/{week}")


if __name__ == "__main__":
    import json

    USERNAME = "tallen21"
    USER_ID = "839972291348639744"
    LEAGUE_ID = "1259602742452690944"
    
    testLeague = League({"league_id": LEAGUE_ID})
    print(json.dumps(testLeague.getMatchupsByWeek(1), indent=4))
