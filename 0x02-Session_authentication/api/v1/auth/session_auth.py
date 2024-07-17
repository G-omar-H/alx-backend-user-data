#!/usr/bin/env python3
"""
session_auth.py
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    Sessionn authentification mechanism
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id

        Args:
            user_id (str, optional): user ID. Defaults to None.

        Returns:
            str: the session instance id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        sessionID = str(uuid.uuid4())
        self.user_id_by_session_id[sessionID] = user_id
        return sessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID

        Args:
            session_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        returns a User instance based on a cookie value

        Args:
            request (_type_, optional): _description_. Defaults to None.
        """
        print(self.user_id_by_session_id)
        if request:
            sessionCookie = self.session_cookie(request)
            if sessionCookie:
                userId = self.user_id_for_session_id(sessionCookie)
                return User.get(userId)
