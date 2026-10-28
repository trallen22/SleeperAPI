from fastapi import FastAPI
from src.models.league import League
from src.models.roster import Roster

app = FastAPI()

@app.get("/api/{league_id}")
async def get_league_info(league_id: int):
    curLeague = League.getSpecificLeagueById(leagueId=league_id)
    return {
        "league_id": curLeague.league_id,
        "name": curLeague.name,
        "season": curLeague.season
    }

@app.get("/api/{league_id}/matchups")
# TODO: remove these defaults
async def get_matchup_info(league_id: int, week: int=7, matchup_id: int=1):
    print(f"week: {week}\t matchup_id: {matchup_id}")
    leagueMatchups = League.getSpecificLeagueById(leagueId=league_id).getMatchupsByWeek(week)
    curMatchup = []
    for m in leagueMatchups:
        if m['matchup_id'] == matchup_id:
            curMatchup.append(m)
    return {
        "roster_1": curMatchup[0]['roster_id'],
        "roster_2": curMatchup[1]['roster_id']
    }

@app.get("/api/{league_id}/roster")
async def get_roster_info(league_id: int, roster_id: int):
    allRosters = League.getSpecificLeagueById(leagueId=league_id).getCurRosters()
    curRoster = Roster.getCurRosterFromLeague(roster_id=roster_id, all_rosters=allRosters)
    return {
        "roster_id": curRoster.roster_id,
        "starters": curRoster.starters,
        "bench": curRoster.bench,
        "taxi": curRoster.taxi_squad
    }