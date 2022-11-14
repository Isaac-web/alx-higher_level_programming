#!/usr/bin/python3
"""
This module fetches all states
that start with the letter N
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    try:
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
        rows = cur.fetchall()

        for r in rows:
            print(r)
    except MySQLdb.Error:
        print("Something went wrong...")
    finally:
        cur.close()
        db.close()
