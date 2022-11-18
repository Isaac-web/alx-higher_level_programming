#!/usr/bin/python3
"""
This script fetches the first state
from the database
"""
if __name__ == "__main__":
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv

    def configure_db(username, password, database):
        """configures a new db engine"""
        str = "mysql://{}:{}@localhost:3306/{}".format(
                username, password, database)
        return create_engine(str)

    try:
        engine = configure_db(argv[1], argv[2], argv[3])
        session = Session(bind=engine)

        state = session.query(State).order_by(State.id).first()
        if not state:
            print("Nothing")
        else:
            print("{}: {}".format(state.id, state.name))
    except Exception as e:
        print(e)
