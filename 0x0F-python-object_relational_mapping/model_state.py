#!/usr/bin/python3
"""
This module contains code that
create a State class that inherits from
Base class and maps to a table in the
mysql database
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy import create_engine


engine = create_engine(
    "mysql+pymysql://root:$$Superdad77@localhost:3306/hbtn_0e_0_usa")

Base = declarative_base()


class State(Base):
    """
    Defines the state domain object
    """
    __tablename__ = "states"
    id = Column(Integer, Sequence(
        "state_id_seq"), nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
