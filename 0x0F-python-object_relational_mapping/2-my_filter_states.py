#!/usr/bin/python3

import MySQLdb
import sys

"""
This script prints the states from the database
the marches the argument passed
"""


def configure_db():
    """
    configures the database connection and returns the db
    connection object
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
    pattern = sys.argv[4]

    try:
        cur.execute(
            "SELECT * FROM states WHERE name = {} ORDER BY id ASC"
            .format(pattern))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as err:
        print("Something went wrong.")
    finally:
        cur.close()
        db.close()
