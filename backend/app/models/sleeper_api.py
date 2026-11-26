import requests

class SleeperApi():
    SLEEPER_BASE_ENDPOINT = "https://api.sleeper.app/"

    # current defaults
    SPORT = "nfl"
    SEASON = "2025"

    # base of APIs
    API_LEAGUE_BASE = "v1/league/"
    API_USER_BASE = "v1/user/"

    @classmethod
    def _callApi(cls, path: str):
        endpoint = f"{cls.SLEEPER_BASE_ENDPOINT}{path}"
        print(f"getting endpoint: {endpoint}")
        return requests.get(endpoint).json()

    @classmethod
    def apiGetSpecificLeagueById(cls, leagueId: str) -> dict:
        return cls._callApi(f"{cls.API_LEAGUE_BASE}{leagueId}")

    @classmethod
    def apiGetCurRostersByLeagueId(cls, leagueId: str) -> list[dict]:
        return cls._callApi(f"{cls.API_LEAGUE_BASE}{leagueId}/rosters")

    @classmethod
    def apiGetUsersByLeagueId(cls, leagueId: str) -> list[dict]:
        return cls._callApi(f"{cls.API_LEAGUE_BASE}{leagueId}/users")

    @classmethod
    def apiGetMatchupsByWeekByLeagueId(cls, leagueId: str, week: int) -> list[dict]:
        return cls._callApi(f"{cls.API_LEAGUE_BASE}{leagueId}/matchups/{week}")

    @classmethod
    def apiGetUser(cls, identifier: str):
        return cls._callApi(f"{cls.API_USER_BASE}{identifier}")

    @classmethod
    def apiGetAllLeaguesForUserId(cls, userId: str, season: str=SEASON, sport: str=SPORT) -> list[dict]:
        return cls._callApi(f"{cls.API_USER_BASE}{userId}/leagues/{sport}/{season}") 