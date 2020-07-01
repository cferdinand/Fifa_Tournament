import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL DBMS


class DB_Connection():

    def __init__(self, dbname, user):
        self.dbname = dbname
        self.user = user
        self.con = self.open_connection()

    def open_connection(self):
        con = psycopg2.connect(f"dbname={self.dbname} user={self.user}")
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        return con

    # Generate a cursor object
    def get_cursor(self):
        self.cursor = self.con.cursor()

        return self.cursor

    # Close the connection
    def close_connection(self):
        self.cursor.close()
        self.con.close()

        return
