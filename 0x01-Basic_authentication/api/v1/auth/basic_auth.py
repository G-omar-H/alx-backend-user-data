#!/usr/bin/env python3
"""
basic_auth.py
"""
from api.v1.auth.auth import Auth


class Basic_auth(Auth):
    """
    Base64 part of the Authorization header for a Basic Authentication
    """
