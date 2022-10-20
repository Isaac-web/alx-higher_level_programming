#!/usr/bin/python3

import MySQLdb
import sys

"""
This script selects the cities in the database
and prints them to the output
"""


def configure_db():
    """
    Returns a DBAPI connection object after
    configuring the database
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    return MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=database)


if __name__ == "__main__":
    db = configure_db()
    cur = db.cursor()

    try:
        cur.execute("SELECT * FROM cities ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as err:
        print("Something went wrong.")
    finally:
        cur.close()
        db.close()
