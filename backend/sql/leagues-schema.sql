drop table if exists leagues;

-- NOTE: this should line up with league object attributes
create table leagues (
    league_id       VARCHAR NOT NULL,
    name            VARCHAR,
    season          VARCHAR,
    season_type     VARCHAR,
    sport           VARCHAR,
    status          VARCHAR,
    total_rosters   VARCHAR,
    roster_positions        VARCHAR,
    previous_league_id      VARCHAR,
    draft_id        VARCHAR,
    league_users    VARCHAR,
    matchups_by_week        VARCHAR,
    scoring_settings        VARCHAR,
    settings        VARCHAR,
    avatar          VARCHAR,
    current_rosters VARCHAR,
    primary key (league_id)
);
