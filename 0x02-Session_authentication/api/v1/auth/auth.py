#!/usr/bin/env python3
"""
Authentification class
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """
    class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if path is an exluded path

        Args:
            path (str):path to check
            excluded_paths (List[str]): list of exluded paths

        Returns:
            bool: true if path is not in exluded paths, else False
        """
        if path is None or excluded_paths is None:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """validate all requests to secure the API

        Args:
            request (object): the data sent from the Client to Server.

        Returns:
            str:  the value of the header request Authorization
        """
        if request is None or 'Authorization' not in request.headers.keys():
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        return the current user ID
        """
        return None

    def session_cookie(self, request=None):
        """
        returns a cookie value from a request

        Args:
            request (_type_, optional): _description_. Defaults to None.
        """
        if request is None:
            return None
        sessionName = os.getenv('SESSION_NAME')
        return request.cookies.get(sessionName)
