from src.db import index
from psycopg2 import DatabaseError


def get_tournaments(name=None):
    """
    Get a list of tournaments by tournament name. 
    If no name is provided all tournaments will be returned
    """

    con = index.DB_Connection("fifa_tournament", "christianferdinand")
    cursor = con.get_cursor()

    if name:
        query = f"SELECT t.id, t.tournament_name, s.name as winner FROM tournaments t JOIN users s ON t.winner=s.id WHERE tournament_name='{name}'"
    else:
        query = "SELECT t.id, t.tournament_name, s.name as winner FROM tournaments t JOIN users s ON t.winner=s.id;"
    cursor.execute(query)

    results = cursor.fetchall()

    results = [{"id": value[0], "name": value[1],
                "winner": value[2]} for value in results]

    con.close_connection()

    return results


def add_tournament(tournament):
    """
    Inserts a tournament into the tournament table 
    and updates the matchups table
    """

    results = None
    try:
        con = index.DB_Connection("fifa_tournament", "christianferdinand")
        cursor = con.get_cursor()

        query = "INSERT INTO tournaments (tournamnet_name,type,number_of_teams,winner) VALUES (%s,%s,%s,%s)"
        values = [value for value in tournament.values()]

        cursor.execute(query, values)
        con.con.commit()

        results = True

    except (DatabaseError) as err:
        results = err
    finally:
        con.close_connection()
        return results


def remove_tournament(tournament):
    pass


def update_tournamet(tournament):
    return True


def get_match_ups(tournament):
    """Get a list of matches by tournament"""

    con = index.DB_Connection("fifa_tournament", "christianferdinand")
    cursor = con.get_cursor()

    tournament_id = tournament["tournament_id"]

    query = f"SELECT * FROM matchup WHERE tournament={tournament_id}"
    cursor.execute(query)

    results = cursor.fetchall()

    con.close_connection()

    return results


def add_player():
    pass
