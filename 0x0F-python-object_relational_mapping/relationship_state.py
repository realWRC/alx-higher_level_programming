#!/usr/bin/python3
"""
python file that contains the class definition of a State and an
instance Base = declarative_base()
"""

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Mapped Stated object"""

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",)
