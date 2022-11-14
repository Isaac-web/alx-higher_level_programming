#!/usr/bin/python3
"""
Returns all cities from the database
"""

import MySQLdb
from sys import argv


def configure_db():
    """
    Returns a db connection
    """
    return MySQLdb.connec(user=argv[1], 
        passwd=argv[2], db=argv[3], host="localhost", port=3306)
    

if __name__ == "__main__":
    db = configure_db()

    try:
        cur = db.cursor();
        cur.execute("SELECT * FROM cities ORDER BY id")
        rows = cur.fetchall()

        for r in rows:
            print(r)
    except MySQLdb.Error:
        print("Something went wrong...")
    finally:
        cur.close()
        db.close()
