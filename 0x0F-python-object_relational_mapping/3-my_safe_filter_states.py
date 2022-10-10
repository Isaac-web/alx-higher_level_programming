#!/usr/bin/python3

import sys
import MySQLdb

"""
This script uses a safer approach to fetch
states database
"""


def configure_db():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    return MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=database)


if __name__ == "__main__":
    db = configure_db()
    cur = db.cursor()
    pattern = sys.argv[4]

    if len(pattern) > 15:
        return

    try:
        cur.execute(
            "SELECT * FROM states WHERE name = {} ORDER BY id"
            .format(pattern)
        )
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except MySQLdb.Error as err:
        print("Something went wrong.")
    finally:
        cur.close()
        db.close()
