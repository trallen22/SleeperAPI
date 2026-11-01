from src.models.sleeper_api import SleeperApi
from src.utils import database_utilities as db_utils
from src import config

class League():
    NUM_STARTERS = 10
    NUM_BENCH = 25

    def __init__(self, leagueInfoDict: dict=None, leagueInfoTuple: tuple=None):
        # TODO: should probably move the different logic to separate class methods
        if leagueInfoDict is not None:
            self.league_id = leagueInfoDict.get("league_id")
            self.name = leagueInfoDict.get("name")
            self.season = leagueInfoDict.get("season")
            self.season_type = leagueInfoDict.get("season_type")
            self.sport = leagueInfoDict.get("sport")
            self.status = leagueInfoDict.get("status")
            self.total_rosters = leagueInfoDict.get("total_rosters")
            self.roster_positions = leagueInfoDict.get("roster_positions")
            self.previous_league_id = leagueInfoDict.get("previous_league_id")
            self.draft_id = leagueInfoDict.get("draft_id")
            self.league_users = None
            self.matchups_by_week = {}
            self.scoring_settings = leagueInfoDict.get("scoring_settings")
            self.settings = leagueInfoDict.get("settings")
            self.avatar = leagueInfoDict.get("avatar")
            self.current_rosters = None
        elif leagueInfoTuple is not None:
            # TODO: this isn't very maintainable; hyper dependent on schema
            self.league_id = leagueInfoTuple[0]
            self.name = leagueInfoTuple[1]
            self.season = leagueInfoTuple[2]
            self.season_type = leagueInfoTuple[3]
            self.sport = leagueInfoTuple[4]
            self.status = leagueInfoTuple[5]
            self.total_rosters = leagueInfoTuple[6]
            self.roster_positions = leagueInfoTuple[7]
            self.previous_league_id = leagueInfoTuple[8]
            self.draft_id = leagueInfoTuple[9]
            self.league_users = leagueInfoTuple[10]
            self.matchups_by_week = {}
            self.scoring_settings = leagueInfoTuple[12]
            self.settings = leagueInfoTuple[13]
            self.avatar = leagueInfoTuple[14]
            self.current_rosters = leagueInfoTuple[15]
        else:
            raise ValueError("Must pass either leagueInfoDict or leagueInfoTuple")

    # class methods
    @classmethod
    def getSpecificLeagueById(cls, leagueId: str) -> "League":
        leagueSQLquery = db_utils.sqlSelect(db_utils.LEAGUES_TABLE, where={ "league_id": leagueId })
        if len(leagueSQLquery) == 0: # we didn't find it in the db
            league = League(leagueInfoDict=SleeperApi.apiGetSpecificLeagueById(leagueId))
            if db_utils.sqlInsert(db_utils.LEAGUES_TABLE, League.convertLeagueObjToTuple(league)):
                print(f"failed to insert league {leagueId} into {db_utils.LEAGUES_TABLE}")
        else:
            print("found in db!")
            league = League(leagueInfoTuple=leagueSQLquery[0])
        return league

    # instance methods
    def getCurRosters(self) -> list[dict]:
        if self.current_rosters is None:
            self.current_rosters = SleeperApi.apiGetCurRostersByLeagueId(self.league_id)
        return self.current_rosters

    def getUsers(self) -> list[dict]:
        if self.league_users is None:
            self.league_users = SleeperApi.apiGetUsersByLeagueId(self.league_id)
        return self.league_users

    def getMatchupsByWeek(self, week: int) -> list[dict]:
        if self.matchups_by_week.get(week) is None:
            # TODO: Nood to make sure the matchup format stays consistent
            matchupsSQLquery = db_utils.sqlSelect(db_utils.MATCHUPS_TABLE, where={ "league_id": self.league_id, "week": week }, output="dict")
            if len(matchupsSQLquery) == 0: # we didn't find any in the db
                print(f"Couldn't find matchups for league '{self.league_id}' week '{week}' into table {db_utils.MATCHUPS_TABLE}")
            else:
                print(f"found matchups for league '{self.league_id}' week '{week}' in db!")
                self.matchups_by_week[week] = matchupsSQLquery
        return self.matchups_by_week.get(week)

    def insertRostersToDBbyWeek(self, week: int) -> int:
        if not self.matchups_by_week:
            self.getMatchupsByWeek(week)
        for m in self.matchups_by_week:
            # print(m)
            # print(f"MATCHUP ID: {m['matchup_id']}")
            # print(f"ROSTER ID: {m['roster_id']}")
            bench = [player for player in m["players"] if player not in m["starters"]]
            # print(f"STARTERS: {m['starters']}")
            # print(f"BENCH: {bench}")
            starters = m["starters"]
            # Should already be 10 starters but just in case; to align with schema
            starters.extend([None] * (len(starters) - self.NUM_STARTERS))
            # print(starters)
            # make sure starters are first
            curLineup = starters + bench
            pointsList = []
            for p in curLineup:
                pointsList.append(p)
                pointsList.append(m["players_points"][p])
            # print(pointsList)
            pointsList.extend([None] * (len(starters) - 1))
            print(len(pointsList))
            # db_utils.sqlInsert(db_utils.ROSTERS_TABLE, )

    @staticmethod
    def convertLeagueObjToTuple(leagueObj) -> tuple:
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
    LEAGUE_ID = config.SMACKERS_LEAGUE_ID_2026
    TEST_WEEK = 7
    
    testLeague = League.getSpecificLeagueById(LEAGUE_ID)
    print(f"all: {testLeague.getMatchupsByWeek(TEST_WEEK)}")
    # for m in testLeague.getMatchupsByWeek(TEST_WEEK):
    #     print(m)
    # testLeague.insertRostersToDBbyWeek(1)
