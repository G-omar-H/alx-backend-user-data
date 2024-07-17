#!/usr/bin/env python3
"""
session_auth.py
"""
from api.v1.auth.auth import Auth
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
