drop table if exists rosters;

-- news_articles holds the information for the individual articles
create table rosters (
    user_id         VARCHAR NOT NULL,
    username        VARCHAR,
    display_name    VARCHAR,
    roster_id       VARCHAR,
    matchup_by_week VARCHAR,
    primary key (user_id)
);
