#!/usr/bin/python3
'''Get all states that match input state, safe from injection1'''


if __name__ == '__main__':
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
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

    # create the state we want to add
    cali = State(name='California')
    cali.cities = [City(name='San Francisco')]

    # add the states to the session
    session.add(cali) 

    session.commit()
