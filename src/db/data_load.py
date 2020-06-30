import requests
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def get_teams():
    headers = {
        "content-type": "application/json",
        "X-AUTH-TOKEN": "fa432bde-27ad-4639-bd19-bed15e0df853"
    }
    clubs = []
    data_collected = 0
    for page in range(1, 39):
        get_club_list = requests.get(
            f"https://futdb.app/api/clubs?page={page}", headers=headers)
        clubs.extend(get_club_list.json()["items"])
        data_collected += get_club_list.json()["count"]

    return clubs


def get_images():
    get_data = requests.get("https://fut.best/api/clubs")
    club_data = get_data.json()["data"]["clubs"]
    result = {}

    for club in club_data:
        result[club["name"]] = club["Image"]["url"]

    return result


def consolidate():
    clubs = get_teams()
    logos = get_images()

    remove_club = {}

    for club in clubs:
        if club["name"] == "Piemonte Calcio":
            remove_club = club
            continue

        if club["name"] == "Juventus":
            juventus_logo = open("../images/Juventus.svg", "rb").read()
            club["logo"] = psycopg2.Binary(juventus_logo)
            continue

        try:
            logo_exists = logos[club["name"]]
            if logo_exists:
                club["logo"] = logo_exists
        except KeyError:
            club["logo"] = None

    clubs.remove(remove_club)

    return clubs


data = consolidate()

try:
    con = psycopg2.connect(
        "dbname=fifa_tournament user=christianferdinand")
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = con.cursor()

    for i, club in enumerate(data):
        command = "INSERT INTO teams (team_name, team_logo) VALUES (%s,%s)"
        values = (club["name"], club["logo"])
        cursor.execute(command, values)

    con.commit()

except (Exception, psycopg2.DatabaseError) as err:
    print("DATABASE ERROR: ", err)
finally:
    cursor.close()
    con.close()
