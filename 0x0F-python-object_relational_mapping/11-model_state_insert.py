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
    str = "mysql://{}:{}@localhost:3306/{}".format(
            username, password, database)
    return create_engine(str)


if __name__ == "__main__":
    try:
        engine = configure_db(argv[1], argv[2], argv[3])
        session = Session(bind=engine)

        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()

        print(new_state.id)
    except Exception as e:
        print(e)
