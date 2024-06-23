#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
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
            "SELECT cities.name FROM cities LEFT JOIN states ON\
            states.id = cities.state_id WHERE states.name = %s\
            ORDER BY cities.id ASC", (argv[4],)
        )
        rows = cur.fetchall()

        strings = []
        for row in rows:
            strings.append(row[0])
        print(", ".join(strings))

    except MySQLdb.Error as e:
        print("MySQL Error: ", e)
    finally:
        if db_connector:
            cur.close()
            db_connector.close()
