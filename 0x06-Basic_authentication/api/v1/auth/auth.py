#!/usr/bin/env python3
"""
auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth():

    """ comment """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
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
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        return None
