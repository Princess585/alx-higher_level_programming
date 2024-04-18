#!/usr/bin/python3
# Defines a city model
# Inherits from SQLAlchemy base and links to the MySQL table cities

from sqlalchemy import column, foreignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class city(base):
    """Represents a city for a MySQL database

    Attributes:
        id (str): The city's id.
        name (sqlalchemy.Integer): The city's name.
        state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = "cities"
    id = column(Integer, primary_key=True)
    name = column(String(128), nullable=False)
    state_id = column(Integer, ForeignKey("states.id"), nullable=False)
