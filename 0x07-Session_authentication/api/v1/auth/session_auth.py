#!/usr/bin/env python3
"""
auth module for the API
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ SessionAuth Class """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ session comment """
        if user_id is None or type(user_id) != str:
            return None
        sess_id = str(uuid4())
        self.user_id_by_session_id[sess_id] = user_id
        return sess_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user_id comment """
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ comment """
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return None
        _id = self.user_id_for_session_id(session_cookie)
        return User.get(_id)
