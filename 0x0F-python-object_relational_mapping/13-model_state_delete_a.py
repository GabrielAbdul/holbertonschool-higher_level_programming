#!/usr/bin/python3
'''Get all states that match input state, safe from injection1'''


if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # define parameters for session
    Session = sessionmaker(bind=engine)

    # create session
    session = Session()

    # query our results
    result = session.query(State).filter(State.name.like('%a%'))

    # print our result, formatted correctly
    for results in result:
        session.delete(results)

    session.commit()
