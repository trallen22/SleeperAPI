drop table if exists roster_stats;

-- roster_stats is season stats for a roster/team
create table roster_stats (
    league_id               VARCHAR NOT NULL,
    roster_id               VARCHAR NOT NULL,
    owner_id                VARCHAR NOT NULL,
    wins                    INT,
    ties                    INT,
    losses                  INT,
    fpts_decimal            REAL,
    fpts_against_decimal    REAL,
    fpts_against            REAL,
    fpts                    REAL,
    waiver_position         INT,
    waiver_budget_used      INT,
    total_moves             INT,
    primary key (league_id, roster_id)
)