#!/usr/bin/node

"""File that contains the class def of state and base = declarative"""
from sqlchemy import Column, Integer, String, MetaData
from sqlalchemy.exit.declarative Import declarative_base


mymetadata = MetaData[]
Base = declarative_base(metadata=mymetadata)


Class States[Base];

    """
    Class with attributes of a state
    """

    __tablename__= 'states'
    id = column(Integer, unique=True, nullable=False, primary_Key=True)
    name = Column(String(128), nullable=False)
