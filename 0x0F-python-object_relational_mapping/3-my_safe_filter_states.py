#!/usr/bin/python3
"""
This script returns all the states
that match the search patten
"""
import MySQLdb
from sys import argv


def configure_db():
    """
    Returns a db connection
    """
    db = MySQLdb.connect(
            user=argv[1], passwd=argv[2], host="localhost",
            port=3306, db=argv[3])

    return db


if __name__ == "__main__":
    db = configure_db()
    cur = db.cursor()
    pattern = argv[4]
    try:
        cur.execute(
            "SELECT * FROM states WHERE BINARY name = '{}'".format(pattern))
        rows = cur.fetchall()
