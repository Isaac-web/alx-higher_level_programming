#!/usr/bin/python3

'''
This script lists all the states
in the database
'''
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            user=username, passwd=password, host='localhost',
            port=3306, db=database)

    cur = db.cursor()

    try:
        cur.execute("SELECT * FROM states states ORDER BY id ASC")
        rows cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as err:
        print("Something went wrong fetching the data.")
    finally:
        cur.close()
        db.close()
