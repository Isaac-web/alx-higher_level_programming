#!/usr/bin/python3
"""
This Module prints the result to a query for a database
"""

import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
        user=username, passwd=password, host='localhost',
        port=3306, db=database)

cur = db.cursor()

try:
    db.execute("SELECT * FROM states states ORDER BY id")
    rows = db.fetchall()
    for row in rows:
        print("({}, '{}')".format(row.id, row.name))
except MySQLdb.Error as err:
    print("Error")
