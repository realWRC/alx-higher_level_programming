#!/usr/bin/python3
"""
python file that contains the class definition of a City and an
instance Base = declarative_base()
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String

class City(Base):
    """Mapped City object"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
