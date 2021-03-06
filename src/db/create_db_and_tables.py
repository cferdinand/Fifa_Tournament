import index as db
from psycopg2 import DatabaseError

# Obtain a DB Cursor
con = db.open_connection("postgres", "christianferdinand")
cursor = con.cursor()


# Create a database in PostgreSQL
name_Database = "fifa_tournament"
sqlCreateDatabase = "create database "+name_Database+";"

cursor.execute(
    f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{name_Database}'")
exists = cursor.fetchone()
if not exists:
    cursor.execute(sqlCreateDatabase)

# Close the postgres connection
db.close_connection(cursor, con)

# Create tables


def create_tables():
    """Creates the tables for the tournament database (user, tournament, teams and matchup)"""

    tournament_tables = {
        "user_table": """
        CREATE TABLE IF NOT EXISTS users (
            id serial PRIMARY KEY,
            name varchar(128),
            stream_link varchar, 
            image varchar,
            wins int
        );""",
        "tournaments_tables": """
        CREATE TABLE IF NOT EXISTS tournaments (
            id serial PRIMARY KEY,
            tournament_name varchar(128),
            winner int
        );""",
        "teams_table": """
        CREATE TABLE IF NOT EXISTS teams (
            id serial PRIMARY KEY,
            team_name varchar(128),
            team_logo varchar
            );
        """,
        "matchup_table": """
        CREATE TABLE IF NOT EXISTS matchup (
            id serial PRIMARY KEY,
            home_player int,
            away_player int,
            home_team int,
            away_team int,
            home_score int,
            away_score int,
            winner int,
            tournament int
            );
        """
    }

    try:
        con = db.open_connection("fifa_tournament", "christianferdinand")
        cursor = con.cursor()

        for command in tournament_tables.values():
            cursor.execute(command)

        con.commit()

    except (Exception, DatabaseError) as err:
        print(err)
    finally:
        cursor.close()
        con.close()


create_tables()
