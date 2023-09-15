#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound, InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_pw: str) -> User:
        """
        Class method that adds a new user to
        the database
        """
        new_user = User(email=email, hashed_password=hashed_pw)

        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Class method that is used for searching a particular user
        via a keyword identifier
        """
        try:
            return self._session.query(User).filter_by(**kwargs).first()
        except NoResultFound:
            raise NoResultFound("No user found with the specified criteria.")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query arguments.")
