#!/usr/bin/python3
"""
Contains the State class that maps to
the states table in the mysql database
and inherits from the Base class
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence


Base = declarative_base()


class State(Base):
    """This maps to the states table in the database"""
    __tablename__ = "states"
    id = Column(Integer, Sequence(
        "state_id_seq"), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
