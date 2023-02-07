#!/usr/bin/env python3
"""
auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        format_path = f'{path}/'
        if path in excluded_paths or format_path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        if request is None:
            return None
        if request.get('Authorization', 0) == 0:
            return None
        else:
            return request.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        return None
