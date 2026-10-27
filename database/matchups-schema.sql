drop table if exists matchups;

-- matchups holds information for specific matchup in a league
create table matchups (
    matchup_id      VARCHAR NOT NULL,
    roster_id       VARCHAR NOT NULL,
    league_id       VARCHAR NOT NULL,
    week            INTEGER,
    total_points    REAL,
    starters        TEXT,
    bench           TEXT,
    reserve         TEXT,
    taxi            TEXT,
    primary key (league_id, week, matchup_id, roster_id),
    foreign key (league_id) REFERENCES leagues(league_id)
)