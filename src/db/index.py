import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL DBMS


def open_connection(dbname, user):
    con = psycopg2.connect(f"dbname={dbname} user={user}")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    return con

# Close the connection


def close_connection(cursor, con):
    cursor.close()
    con.close()

    return
