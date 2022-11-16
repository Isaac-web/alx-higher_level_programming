#!/usr/bin/python3

import sys
import MySQLdb

"""
This script takes the name of a state as
an agument and prints its corresponding
cities in the database
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
    state_name = sys.argv[4]

    try:
        cur.execute(
            """
               SELECT *
               FROM cities
               WHERE state_id = (
                    SELECT id
                    FROM states
                    WHERE name = {}
                )
            """.format(state_name)
        )

        rows = cur.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as err:
        print("Something went wrong.")
