#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':

    try:
        db_connector = db.connect(
            host="localhost", user=argv[1],
            port=3306, passwd=argv[2],
            db=argv[3]
        )

        cur = db_connector.cursor()
        cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '%N' \
            ORDER BY states.id ASC"
        )
        rows = cur.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: ", e)
    finally:
        if db_connector:
            cur.close()
            db_connector.close()
