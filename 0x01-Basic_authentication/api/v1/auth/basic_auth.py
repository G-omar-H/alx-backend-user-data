#!/usr/bin/env python3
"""
basic_auth.py
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Base64 part of the Authorization header for a Basic Authentication
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization
        header for a Basic Authentication

        Args:
            authorization_header (str): _description_

        Returns:
            str: _description_
        """
        if authorization_header is None or not isinstance(
            authorization_header, str)\
                or authorization_header[0: 6] != 'Basic ':
            return None
        return authorization_header[6:]
