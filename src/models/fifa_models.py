import psycopg2
from src.db import index as db


def get_tournaments(name=""):
    con = db.open_connection("fifa_tournament", "christianferdinand")
    cursor = con.cursor()

    query = f"SELECT * FROM tournaments WHERE tournament_name='{name}'"
    cursor.execute(query)
    print(cursor.fetchall())


get_tournaments("Covid_Euros")
