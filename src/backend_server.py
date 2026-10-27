from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from src.models.league import League

app = Flask(__name__)

api = Api(app)
CORS(app)

class LeagueInfo(Resource):
    def get(self, league_id):
        curLeague = League.getSpecificLeagueById(leagueId=league_id)
        return {
            "league_id": curLeague.league_id,
            "name": curLeague.name,
            "season": curLeague.season
        }


api.add_resource(LeagueInfo, "/<league_id>")

if __name__ == "__main__":
    app.run(debug=True)