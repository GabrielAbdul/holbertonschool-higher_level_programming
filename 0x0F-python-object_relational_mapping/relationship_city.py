#!/usr/bin/python3
'''Cities in state'''
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''class City inherits from Base'''

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
