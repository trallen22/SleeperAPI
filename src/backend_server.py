from fastapi import FastAPI
from src.models.league import League

app = FastAPI()

@app.get("/api/{league_id}")
async def get_league_info(league_id):
    curLeague = League.getSpecificLeagueById(leagueId=league_id)
    return {
        "league_id": curLeague.league_id,
        "name": curLeague.name,
        "season": curLeague.season
    }
