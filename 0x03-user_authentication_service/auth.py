#!/usr/bin/env python3
"""
auth.py
"""
import bcrypt
from user import User
from db import DB
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    hash the user password
    Args:
        userPwd (str): _description_
    Returns:
        str: _description_
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    generate UUID
    """
    return str(uuid.uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register new user

        Args:
            email (str): _description_
            password (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            User: _description_
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        credentials validation

        Args:
            email (str): _description_
            password (str): _description_

        Returns:
            bool: _description_
        """
        try:
            user = self._db.find_user_by(email=email)
            if not bcrypt.checkpw(
                    password.encode('utf-8'),
                    user.hashed_password):
                return False
            return True

        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        create a session id for the reistred user

        Args:
            email (str): _description_

        Returns:
            str: _description_
        """
        try:
            user = self._db.find_user_by(email=email)
            sessionId = _generate_uuid()
            self._db.update_user(user.id, session_id=sessionId)
            return sessionId
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        get user by session id

        Args:
            session_id (str): _description_

        Returns:
            User: _description_
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
