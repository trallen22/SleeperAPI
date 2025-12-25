drop table if exists users;

-- news_articles holds the information for the individual articles
create table users (
    user_id         VARCHAR NOT NULL,
    username        VARCHAR,
    display_name    VARCHAR,
    roster_id       VARCHAR,
    matchup_by_week VARCHAR,
    primary key (user_id)
);
