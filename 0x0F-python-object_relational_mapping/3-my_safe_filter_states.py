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

    host_name = 'localhost'
    port_number = 3306
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]

    try:
        db_connector = MySQLdb.connect(
            host=host_name, port=port_number,
            user=user_name, passwd=password,
            db=db_name, charset="utf8"
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
