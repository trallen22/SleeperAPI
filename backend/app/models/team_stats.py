from app.models.sleeper_api import SleeperApi
from app.models.league import League
from app.core import config
import pprint

class TeamStats():
    def __init__(self, league_id: str, roster_id: str):
        resp = SleeperApi.apiGetCurRostersByLeagueId(leagueId=league_id)
        pprint.pprint(resp)
        for t in resp:
            if str(t['roster_id']) == str(roster_id):
                # TODO: can't remember what this was intended for
                print("idk")


if __name__ == "__main__":
    test = TeamStats(league_id=config.SMACKERS_LEAGUE_ID_2026, roster_id=1)
