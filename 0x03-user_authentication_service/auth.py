#!/usr/bin/env python3
"""
auth.py
"""
import bcrypt


def _hash_password(userPwd: str) -> str:
    """
    hash the user password
    Args:
        userPwd (str): _description_
    Returns:
        str: _description_
    """
    bytes = userPwd.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)
