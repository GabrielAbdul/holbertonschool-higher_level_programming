#!/usr/bin/python3
'''Get all states that match input state, safe from injection1'''


if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker as sm

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # define parameters for session
    Session = sm(bind=engine)

    # create session
    session = Session()

    state = session.query(State).filter(State.id == 2).one()

    state.name = 'New Mexixo'
    session.commit()
