#!/usr/bin/python3
"""
Returns all cities from the database
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user="root", 
            passwd="$$Superdad77", host="localhost", db="hbtn_0e_4_usa")
    
    cur = db.cursor()

    try:
        cur.execute("SELECT * FROM cities ORDER BY id")
        rows = cur.fetchall()
        for r in rows:
            print(r)
    except MySQLdb.Error:
        print("Somethig went wrong...")
    finally:
        cur.close()
        db.close()

