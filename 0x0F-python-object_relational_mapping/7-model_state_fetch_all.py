#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sys import argv

host = 'localhost'
port = '3306'
username = argv[1]
password = argv[2]
database = argv[3]

try:
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@{host}\
    :{port}/{database}")

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

except SQLAlchemyError as e:
    print(f"An error occured: {e}")

finally:
    if session:
        session.close()
