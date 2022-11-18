#!/usr/bin/python3
"""
This module contains a States class that
maps to a states table in the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


def configure_db(username, password, database):
    """configures a new db engine"""
    str = "mysql+pymysql://{}:{}@localhost:3306/{}".format(
            username, password, database)
    return create_engine(str)


if __name__ == "__main__":
    try:
        username = argv[1]
        password = argv[2]
        db = argv[3]
        engine = configure_db(username, password, db)
        session = Session(bind=engine)

        states = session.query(State).order_by(State.id).all()
        for s in states:
            print("{}: {}".format(s.id, s.name))
    except Exception as e:
        pass
