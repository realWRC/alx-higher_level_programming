#!/usr/bin/python3
"""
Script that takes in arguments and displays all values
in the states table of hbtn_1e_0_usa where name matches
the argument. But this time, write one that is safe from
MySQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    try:
        db_connector = MySQLdb.connect(
            host='localhost', port=3306,
            user=argv[1], passwd=argv[2],
            db=argv[3], charset="utf8"
        )

        cur = db_connector.cursor()
        cur.execute(
            "SELECT * FROM states WHERE name = %s \
            ORDER BY states.id ASC", (argv[4],)
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
