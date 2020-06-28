import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_tables():
    """Creates the tables for the tournament database (user, tournament, teams and matchup)"""

    tournament_tables = {
        "user_table": """
        CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, name varchar(128), image varchar
        );
        """,
        "tournaments_tables": """
        CREATE TABLE IF NOT EXISTS tournaments (id serial PRIMARY KEY, tournament_name varchar(128), image varchar);
        """,
        "teams_table": """
        CREATE TABLE IF NOT EXISTS teams (id serial PRIMARY KEY, team_name varchar(128), team_logo varchar);
        """,
        "matchup_table": """
        CREATE TABLE IF NOT EXISTS matchup (id serial PRIMARY KEY, home_player int, away_player int, home_team int, away_team int, home_score int, away_score int, winner int, tournament int);
        """
    }

    try:
        con = psycopg2.connect(
            "dbname=fifa_tournament user=christianferdinand")
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = con.cursor()

        for command in tournament_tables.values():
            cursor.execute(command)

    except (Exception, psycopg2.DatabaseError) as err:
        print(err)
    finally:
        cursor.close()
        con.close()
