#!/usr/bin/python3
'''Get all states that match input state, safe from injection1'''


if __name__ == '__main__':
    import sqlalchemy
    import sys
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker as sm

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
                           '.format(sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # need to create a session
    Session = sm(bind=engine)
    session = Session()

    result = session.query(State).all()

    for results in result:
        print("{}: {}".format(results.id, results.name))
