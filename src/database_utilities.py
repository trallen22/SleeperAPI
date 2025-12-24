import sqlite3

# database connection variables
# TODO: need a way to not have to comment this
DATABASE = "../sleeper_fantasy.db"
DEFAULT_VALUE = "Null"
# table names
PLAYERS_TABLE = "players"
LEAGUES_TABLE = "leagues"
# test variables
TEST_TABLE = "ticker_news"
TEST_TICKER = "MSFT"
TEST_RELATED = [ "AMZN", "NVDA", "DIS" ]
TEST_DATE = "2025-06-06"
TEST_INSERT = (TEST_TICKER, f'{TEST_RELATED}', TEST_DATE)
TEST_SELECT_COLS = [ "ticker_symbol", "related_tickers" ]
# debug flag
DB_UTILS_DEBUG = 0

# we'll try to open a connection 
try: 
    connection = sqlite3.connect(DATABASE) 
except Exception as e:
    print(f"ERROR: failed to connect to database")
    print(f'error: {e}')
    exit(1)

def sqlInsert(table: str, curTuple: tuple[str,str,str]) -> int:
    """
    sqlInsert: executes a SQL insert statement on a given table \\
    parameters: \\
        table - str, name of table to insert values into \\
        curTuple - tuple, tuple of values to insert into table \\
    returns: \\
        0 - success \\
        1 - connection failed \\
        2 - execution failed
    """
    curCursor = connection.cursor()
    # actually inserting into the table
    try:
        # we build the insert tuple as a string so we can use DEFAULT for Postgres SERIAL types
        tupleStr = "("
        for i in range(len(curTuple)):
            # if curTuple[i] is not None:
            #     tupleStr += f"'{curTuple[i]}', "
            # else: # use default if None was passed for value
            #     tupleStr += f"{DEFAULT_VALUE}, "
            tupleStr += "?, "
        tupleStr = tupleStr[:-2]
        tupleStr += ")"
        sqlStr = f"INSERT INTO {table} VALUES {tupleStr};"
        DB_UTILS_DEBUG and print(f"insert statement: {sqlStr}")
        curCursor.execute(sqlStr, curTuple)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"failed insert '{tupleStr}' into '{table}'")
        print(f"ERROR: {e}")
        return 2
    # cleanup
    curCursor.close()
    return 0

def sqlSelect(table: str, select: list[str]=None, join: list[str]=None, where: dict=None) -> list[tuple]:
    """
    sqlSelect: executes a SQL select statement on a given table \\
    parameters: \\
        table - str, name of table to select values from \\
        select - list, column names to select from \\
        join - list, list of join statements \\
        where - dict, \\
    returns: a list of tuples replresenting the query results
    """
    curCursor = connection.cursor()
    # setup SELECT str
    columnStr = ""
    if select:
        for col in select:
            columnStr += f"{col}, "
        columnStr = columnStr[:-2]
    else:
        columnStr = "*"
    # setup JOIN string
    joinStr = ""
    # TODO: Not sure if having 'join' as a list is best but it should be fine for now
    if join:
        joinStr = f" JOIN {join[0]} ON {join[1]}={join[2]}"
    # setup WHERE string
    whereStr = ""
    if where:
        whereStr = " WHERE "
        for key in list(where.keys()):
            whereStr += f"{key}='{where[key]}'"
    # running the sql statement
    sqlStr = f"SELECT {columnStr} FROM {table}{joinStr}{whereStr};"
    DB_UTILS_DEBUG and print(f"sql statement: {sqlStr}")
    try:
        curCursor.execute(sqlStr)
        connection.commit()
        # fetching the results
        queryResults = curCursor.fetchall()
    except Exception as e:
        connection.rollback()
        print(f"failed table: {table}")
        print(f"ERROR: {e}")
        queryResults = []
    # cleanup
    curCursor.close()
    return queryResults

def sqlDelete(table: str, where: dict=None) -> int:
    """
    sqlDelete: executes a SQL delete statement on a given table \\
    parameters: \\
        table - str, name of table to select values from \\
        where - dict, \\
    returns: \\
        0 - success \\
        1 - failed to execute sql command
    """
    curCursor = connection.cursor()
    # setup WHERE string
    whereStr = ""
    if where:
        whereStr = " WHERE "
        for key in list(where.keys()):
            whereStr += f"{key}='{where[key]}'"
    # running the sql statement
    sqlStr = f"DELETE FROM {table}{whereStr};"
    try:
        curCursor.execute(sqlStr)
        connection.commit()
    except Exception as e:
        connection.rollback()
        print(f"failed table: {table}")
        print(f"ERROR: {e}")
        return 1
    # cleanup
    curCursor.close()
    return 0

if __name__ == "__main__":
    print(sqlSelect(PLAYERS_TABLE))