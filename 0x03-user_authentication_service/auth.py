#!/usr/bin/env python3
"""
auth.py
"""
import bcrypt


def _hash_password(password: str) -> str:
    """
    hash the user password
    Args:
        userPwd (str): _description_
    Returns:
        str: _description_
    """
    return bcrypt.hashpw(userPwd.encode('utf-8'), bcrypt.gensalt())
