import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from table import create_tables


# Connect to PostgreSQL DBMS

con = psycopg2.connect("dbname=postgres user=christianferdinand")

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


# Obtain a DB Cursor

cursor = con.cursor()

name_Database = "fifa_tournament"


# Create a database in PostgreSQL

sqlCreateDatabase = "create database "+name_Database+";"
cursor.execute(
    f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{name_Database}'")
exists = cursor.fetchone()
if not exists:
    cursor.execute(sqlCreateDatabase)


cursor.close()
con.close()

# Create tables in PostgreSQL database

create_tables()
