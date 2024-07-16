#!/usr/bin/env python3
"""
basic_auth.py
"""
from api.v1.auth.auth import Auth
from models.user import User
from models.base import Base
from typing import TypeVar
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        return the decoded value of a Base64 string base64_authorization_header

        Args:
            base64_authorization_header (str): _description_

        Returns:
            str: _description_
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except base64.binascii.Error as err:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value.

        Args:
            self (_type_): _description_
            str (_type_): _description_
        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header,
                str) or ':' not in decoded_base64_authorization_header:
            return None, None
        return decoded_base64_authorization_header.split(
            ':')[0], decoded_base64_authorization_header.split(':')[1]

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password.

        Args:
            self (_type_): _description_
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        users = User.search({'email': user_email})
        if not users or users == {}:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
