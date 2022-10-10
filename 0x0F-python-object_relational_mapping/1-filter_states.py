#!/usr/bin/python3

import MySQLdb
import sys

'''
This script lists all the states staring with N 
in the states table
'''

def configure_db():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    return MySQLdb.connect(host='localhost', port=3306,
            user=username, passwd=password, db=database)

if __name__ == "__main__":
    db = configure_db()
    cur = db.cursor()

    try:
        cur.execute(
                "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cur.fetchall()

        for row in rows:
            print(row)
    except MySQL.Error as err:
        print("Error reading data")
    finally:
        cur.close()
        db.close()
    
    
