#!/bin/usr/python3
"""script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            username=sys.argv[1],
            password=sys.argv[2],
            dbname=sys.argv[3],
            state_name=sys.argv[4]
            )
    cursor = db.cursor()

    query = "SELECT * FROM state WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sate_name)

    cursor.execute(query)
    data = cursor.fetchall()

    for state in data:
        print(state)

    cursor.close()
    db.close()
