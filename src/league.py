from operator import le
from time import sleep
import sleeper_api
import database_utilities as db_utils

class League():
    SPORT = "nfl"
    SEASON = "2025"

    def __init__(self, leagueInfo: dict):
        self.league_id = leagueInfo.get("league_id")
        self.name = leagueInfo.get("name")
        self.season = leagueInfo.get("season")
        self.season_type = leagueInfo.get("season_type")
        self.sport = leagueInfo.get("sport")
        self.status = leagueInfo.get("status")
        self.total_rosters = leagueInfo.get("total_rosters")
        self.roster_positions = leagueInfo.get("roster_positions")
        self.previous_league_id = leagueInfo.get("previous_league_id")
        self.draft_id = leagueInfo.get("draft_id")
        self.league_users = None
        self.matchups_by_week = {}
        self.scoring_settings = leagueInfo.get("scoring_settings")
        self.settings = leagueInfo.get("settings")
        self.avatar = leagueInfo.get("avatar")
        self.current_rosters = None

    # class methods
    @classmethod
    def getSpecificLeagueById(cls, leagueId: str) -> "League":
        leagueSQLquery = db_utils.sqlSelect(db_utils.LEAGUES_TABLE, { "league_id": leagueId })
        if len(leagueSQLquery) == 0: # we didn't find it in the db
            league = League(cls._apiGetSpecificLeagueById(leagueId))
            if db_utils.sqlInsert(db_utils.LEAGUES_TABLE, League.convertLeagueObjToTuble(league)):
                print(f"failed to insert league {leagueId} into {db_utils.LEAGUES_TABLE}")
        else:
            print("found in db!")
            league = None
        return league

    @classmethod
    def _apiGetSpecificLeagueById(cls, leagueId: str) -> dict:
        return sleeper_api.callApi(f"v1/league/{leagueId}")

    # instance methods
    def getCurRosters(self) -> list[dict]:
        if self.current_rosters is None:
            self.current_rosters = self._apiGetCurRostersByLeagueId()
        return self.current_rosters

    def getUsers(self) -> list[dict]:
        if self.league_users is None:
            self.league_users = self._apiGetUsersByLeagueId()
        return self.league_users

    def getMatchupsByWeek(self, week: int) -> list[dict]:
        if self.matchups_by_week.get(week) is None:
            self.matchups_by_week[week] = self._apiGetMatchupsByWeekByLeagueId(week)
        return self.matchups_by_week[week]

    # private instance methods
    def _apiGetCurRostersByLeagueId(self) -> list[dict]:
        return sleeper_api.callApi(f"v1/league/{self.league_id}/rosters")

    def _apiGetUsersByLeagueId(self) -> list[dict]:
        return sleeper_api.callApi(f"v1/league/{self.league_id}/users")

    def _apiGetMatchupsByWeekByLeagueId(self, week: int) -> list[dict]:
        return sleeper_api.callApi(f"v1/league/{self.league_id}/matchups/{week}")

    @staticmethod
    def convertLeagueObjToTuble(leagueObj) -> tuple:
        # NOTE: make sure this lines up with schema !!
        leagueTuple = (
            leagueObj.league_id,
            leagueObj.name,
            leagueObj.season,
            leagueObj.season_type,
            leagueObj.sport,
            leagueObj.status,
            leagueObj.total_rosters,
            (leagueObj.roster_positions if not isinstance(leagueObj.roster_positions, list) else leagueObj.roster_positions[0]),
            leagueObj.previous_league_id,
            leagueObj.draft_id,
            None, # TODO: implement this dict -> leagueObj.league_users,
            None, # TODO: implement this dict -> leagueObj.matchups_by_week,
            None, # TODO: implement this dict -> leagueObj.scoring_settings,
            None, # TODO: implement this dict -> leagueObj.settings,
            leagueObj.avatar,
            leagueObj.current_rosters
        )
        return leagueTuple

if __name__ == "__main__":
    import json

    USERNAME = "tallen21"
    USER_ID = "839972291348639744"
    LEAGUE_ID = "1259602742452690944"
    
    testLeague = League.getSpecificLeagueById(LEAGUE_ID)
    # testTuple = League.convertLeagueObjToTuble(testLeague)
    # for i in testTuple:
    #     print(i)
    # db_utils.sqlInsert(db_utils.LEAGUES_TABLE, testTuple)
    # print(db_utils.sqlSelect(db_utils.LEAGUES_TABLE, { "league_id": LEAGUE_ID }))
    