#!/usr/bin/python3
"""
This module defines a SQLAchamey
domain object
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


Base.metadata.create_all(engine)
