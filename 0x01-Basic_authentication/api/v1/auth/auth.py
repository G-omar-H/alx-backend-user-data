#!/usr/bin/env python3
"""
Authentification class
"""
from flask import request
from typing import List, TypeVar


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
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_
        """
        return None
