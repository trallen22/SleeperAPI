from src.models.sleeper_api import SleeperApi

class User():
    def __init__(self, username: str=None, user_id: str=None, display_name: str=None, roster_id: str=None) -> None:
        if not (username or user_id):
            raise ValueError("instance must set atleast username or user_id before running _apiGetUser()")
        self.user_id = user_id
        self.username = username
        self.display_name = display_name
        self.setBasicUserInfo()
        self.roster_id = roster_id
        self.matchup_by_week = None # this will need to refactor for different seasons

    def setBasicUserInfo(self) -> str:
        identifier = ""
        if self.username:
            identifier = self.username
        elif self.user_id:
            identifier = self.user_id
        userInfo = SleeperApi.apiGetUser(identifier)
        self.username = userInfo.get("username")
        self.user_id = userInfo.get("user_id")
        self.display_name = userInfo.get("display_name")

    def getAllLeaguesForUserId(self, season=SleeperApi.SEASON, sport=SleeperApi.SPORT) -> list:
        listLeagues = SleeperApi.apiGetAllLeaguesForUserId(userId=self.user_id, season=season, sport=sport)
        return listLeagues

    # def _apiGetUser(self) -> dict:
    #     identifier = ""
    #     if self.username:
    #         identifier = self.username
    #     elif self.user_id:
    #         identifier = self.user_id
    #     return sleeper_api._callApi(f"v1/user/{identifier}")

    # def _apiGetAllLeaguesForUserId(self) -> list[dict]:
    #     return sleeper_api._callApi(f"v1/user/{self.user_id}/leagues/{self.SPORT}/{self.SEASON}") 

if __name__ == "__main__":
    USERNAME = "tallen21"
    testUser = User(USERNAME)
    print(testUser.user_id)