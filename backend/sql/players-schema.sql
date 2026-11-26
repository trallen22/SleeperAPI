drop table if exists players;

-- news_articles holds the information for the individual articles
create table players (
    player_id       VARCHAR NOT NULL,
    first_name      VARCHAR,
    last_name       VARCHAR,
    full_name       VARCHAR,
    stats_id        VARCHAR,
    college         VARCHAR,
    position        VARCHAR,
    fantasy_positions   VARCHAR,
    team            VARCHAR,
    team_abbr       VARCHAR,
    primary key (player_id)
);
