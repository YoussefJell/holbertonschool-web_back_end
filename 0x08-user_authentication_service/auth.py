#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ comment init """
        self._db = DB()

    def register_user(self):
        """ comment register """
        pass


def _hash_password(password: str) -> str:
    """ comment hash pass """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
