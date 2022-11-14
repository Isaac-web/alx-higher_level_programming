#!/usr/bin/python3
"""
This module fetches all states
that start with the letter N
"""
import MySQLdb
import sys


def configure_db():
    """Connects to the database"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            user=username, passwd=password, host="localhost", db=database)
    return db


if __name__ == "__main__":
    db = configure_db()
    cur = db.cursor()

    result = cur.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER_BY id")

    for state in result.fetch_all():
        print(state, end="\n")
