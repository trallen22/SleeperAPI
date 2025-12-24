from base_sleeper_api import BaseSleeperAPI

class User(BaseSleeperAPI):
    SPORT = "nfl"
    SEASON = "2025"

    def __init__(self, username: str=None, user_id: str=None, display_name: str=None, roster_id: str=None) -> None:
        if not (username or user_id):
            raise ValueError("instance must set atleast username or user_id before running _apiGetUser()")
        self.username = username
        self.user_id = user_id
        self.display_name = display_name
        self.setBasicUserInfo()
        self.roster_id = roster_id
        self.matchup_by_week = None # this will need to refactor for different seasons

    def setBasicUserInfo(self) -> str:
        userInfo = self._apiGetUser()
        self.username = userInfo.get("username")
        self.user_id = userInfo.get("user_id")
        self.display_name = userInfo.get("display_name")

    def getAllLeaguesForUserId(self) -> list:
        listLeagues = self._apiGetAllLeaguesForUserId()
        return listLeagues

    def _apiGetUser(self) -> dict:
        identifier = ""
        if self.username:
            identifier = self.username
        elif self.user_id:
            identifier = self.user_id
        return super().callApi(f"v1/user/{identifier}")

    def _apiGetAllLeaguesForUserId(self) -> list[dict]:
        return super().callApi(f"v1/user/{self.user_id}/leagues/{self.SPORT}/{self.SEASON}") 

if __name__ == "__main__":
    USERNAME = "tallen21"
    testUser = User(USERNAME)
    print(testUser.user_id)