#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

try:
    db_connector = MySQLdb.connect(
        host='localhost', user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )

    cur = db_connector.cursor()
    cur.execute(f'SELECT * FROM states ORDER BY id')
    rows = cur.fetchall()

    for row in rows:
        print(row)

except MySQLdb.Error as e:
    print("MySQL Error: ", e)
finally:
    if db_connector:
        cur.close()
        db_connector.close()
