#!/usr/bin/python3
'''add the state object Louisianna'''


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

    # create new state object
    new_state = State(name='Louisiana')

    # add our new state
    session.add(new_state)

    # commit changes to session
    session.commit()

    # print our result, formatted correctly
    print(new_state.id)
