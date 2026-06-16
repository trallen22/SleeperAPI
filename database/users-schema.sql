drop table if exists users;

-- users holds the information for the people in the league
create table users (
    user_id         VARCHAR NOT NULL,
    username        VARCHAR,
    display_name    VARCHAR,
    primary key (user_id)
);
