#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """
    lists all State objects from the
    database hbtn_0e_6_usa
    """

    host = 'localhost'
    port = 3306
    username = argv[1]
    password = argv[2]
    database = argv[3]

    try:
        string = "mysql+mysqldb://{}:{}@{}:\
        {}/{}".format(username, password, host, port, database)
        engine = create_engine(string)

        Session = sessionmaker(bind=engine)
        session = Session()
        new = State(name="Louisiana")
        session.add(new)
        session.commit()

        print('{0}'.format(new.id))

    except SQLAlchemyError as e:
        print(f"An error occured: {e}")

    finally:
        if session:
            session.close()
