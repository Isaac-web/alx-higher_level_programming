#!/usr/bin/python3
"""
Contains the State class that maps to 
the states table in the mysql database 
and inherits from the Base class
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
