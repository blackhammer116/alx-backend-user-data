#!/usr/bin/env python3
"""
Declarative_base: used to declare the User model in sqlalchemy
Integer, Column, String: used for declaring table attributes and columns
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String


Base = declarative_base()

class User(Base):
    """
    User: Model for users table
    The following attributes are to be set for
    users table values.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
