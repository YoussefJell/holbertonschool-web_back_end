#!/usr/bin/env python3
"""
auth module for the API
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ comment class comment class comment class  """

    def extract_base64_authorization_header(self, authorization_header: str
                                            ) -> str:
        """ base64base64 base64 """
        if authorization_header is None:
            return None
        if not type(authorization_header) == str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        base = authorization_header.split(' ')
        return base[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ decoded b64 decoded b64 decoded b64 decoded b64 """
        if base64_authorization_header is None:
            return None
        if not type(base64_authorization_header) == str:
            return None
        try:
            baseEncode = base64_authorization_header.encode('utf-8')
            baseDecode = b64decode(baseEncode)
            return baseDecode.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ return mail n pass return mail n pass return mail n pass """
        if decoded_base64_authorization_header is None:
            return None, None
        if not type(decoded_base64_authorization_header) == str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        userPass = decoded_base64_authorization_header.split(':')
        return userPass[0], userPass[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ return user if correct return user if correct return user if correct """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ retrieve user instance """
        try:
            header = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(header)
            decodeValue = self.decode_base64_authorization_header(base64Header)
            userPass = self.extract_user_credentials(decodeValue)
            user = self.user_object_from_credentials(userPass[0], userPass[1])
            return user
        except Exception:
            return None
