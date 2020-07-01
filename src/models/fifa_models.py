from src.db import index


def get_tournaments(name=None):
    """
    Get a list of tournaments by tournament name. 
    If no name is provided all tournaments will be returned
    """

    con = index.DB_Connection("fifa_tournament", "christianferdinand")
    cursor = con.get_cursor()

    if name:
        query = f"SELECT * FROM tournaments WHERE tournament_name='{name}'"
    else:
        query = "SELECT * FROM tournaments;"
    cursor.execute(query)

    results = cursor.fetchall()
    con.close_connection()

    return results


def add_tournament(tournament):
    """
    Inserts a tournament into the tournament table 
    and updates the matchups table
    """

    con = index.DB_Connection("fifa_tournament", "christianferdinand")
    cursor = con.get_cursor()

    query = "INSERT INTO tournaments (tournamnet_name,type,number_of_teams,winner) VALUES (%s,%s,%s,%s)"
    values = [value for value in tournament.values()]

    cursor.execute(query, values)
    con.con.commit()

    return


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
