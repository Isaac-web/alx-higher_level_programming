#!/usr/bin/python3
"""
This module contains a States class that
maps to a states table in the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv
