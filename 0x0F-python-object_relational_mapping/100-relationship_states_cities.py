#!/usr/bin/python3
"""
script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""

from relationship_state import Base, State
from relationship_city import City
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
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name='California')
        new_city = City(name='San Francisco')
        new_state.cities.append(new_city)

        session.add(new_state)
        session.commit()

    except SQLAlchemyError as e:
        print(f"An error occured: {e}")

    finally:
        if session:
            session.close()
