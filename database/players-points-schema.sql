drop table if exists players_points;

create table players_points (
    league_id       VARCHAR NOT NULL,
    week            INTEGER,
    player_id       INTEGER,
    points          REAL,
    PRIMARY KEY (league_id, week, player_id),
    FOREIGN KEY (league_id, week) REFERENCES matchups(league_id, week),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
)