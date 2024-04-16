#!/usr/bin/python3

"""File that contains the class def of state and base = declarative"""
from sqlchemy import Column, Integer, String, MetaData
from sqlalchemy.exit.declarative Import declarative_base


mymetadata = MetaData[]
Base = declarative_base(metadata=mymetadata)


class States (Base):
    """Represents a state for the MySQL database.

    __tablename__ (str): The name of the MySQL table to store states.
    id (sqlalchemy.Integer): The states's id.
    name (sqlalchemy.String): The states's name.
    """
    __tablename__= "states"
    id = Column(String(128), nullable=False)
