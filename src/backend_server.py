from fastapi import FastAPI
from src.models.league import League
from src.models.player import Player
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
    print(f"\n\n{leagueMatchups}\n\n")
    curMatchup = []
    for m in leagueMatchups:
        if int(m['matchup_id']) == matchup_id:
            curMatchup.append(m)
    return {
        "roster_1": curMatchup[0]['roster_id'],
        "roster_2": curMatchup[1]['roster_id']
    }

@app.get("/api/{league_id}/matchups/{roster_id}")
async def get_matchup_roster(league_id: int, week: int, roster_id: int):
    # TODO: could probably move this to helper function
    print(f"week: {week}\t roster_id: {roster_id}")
    leagueMatchups = League.getSpecificLeagueById(leagueId=league_id).getMatchupsByWeek(week)
    curMatchup = None
    for m in leagueMatchups:
        if (int(m['roster_id']) == roster_id):
            curMatchup = m
            break

    # TODO: could probably improve this logic
    print(f"starters: {curMatchup.get('starters')}")
    players = Player.convertListOfIDs(curMatchup.get("starters"))
    for p in players:
        print(p.full_name)
        p.getPointsByWeek(league_id=league_id, week=week)
    print(f"bench: {curMatchup.get('bench')}")
    bench_players = Player.convertListOfIDs(curMatchup.get("bench"))
    for b in bench_players:
        print(b.full_name)
        b.getPointsByWeek(league_id=league_id, week=week)
    print(f"reserve: {curMatchup.get('reserve')}")
    reserve = Player.convertListOfIDs(curMatchup.get("reserve"))
    for r in reserve:
        print(r.full_name)
        r.getPointsByWeek(league_id=league_id, week=week)
    print(f"taxi: {curMatchup.get('taxi')}")
    taxi_players = Player.convertListOfIDs(curMatchup.get("taxi"))
    for t in taxi_players:
        print(t.full_name)
        t.getPointsByWeek(league_id=league_id, week=week)

    return {
        "starters": [(p.full_name, p.weekly_points.get(f"{week}")) for p in players],
        "bench": [(b.full_name, b.weekly_points.get(f"{week}")) for b in bench_players],
        "reserve": [(r.full_name, r.weekly_points.get(f"{week}")) for r in reserve],
        "taxi": [(t.full_name, t.weekly_points.get(f"{week}")) for t in taxi_players]
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