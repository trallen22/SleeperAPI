drop table if exists league_rosters;

-- holds the mapping for user to roster for a league
CREATE TABLE league_rosters (
    league_id TEXT NOT NULL,
    roster_id INTEGER NOT NULL,
    user_id TEXT,
    PRIMARY KEY (league_id, roster_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);