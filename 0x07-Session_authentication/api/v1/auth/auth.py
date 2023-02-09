#!/usr/bin/env python3
"""
auth module for the API
"""
from os import getenv
from flask import request
from typing import List, TypeVar


class Auth():
    """ comment """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ comment """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ comment """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ comment """
        return None
    def session_cookie(self, request=None):
        if request is None:
            return None
        _my_session_id = getenv("SESSION_NAME")
        return request.cookies.get(_my_session_id)