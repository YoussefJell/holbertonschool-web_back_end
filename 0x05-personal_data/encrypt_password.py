#!/usr/bin/env python3
""" encrypt passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """ hashes a password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ checks if password is valid """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
