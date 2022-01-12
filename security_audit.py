#!/usr/bin/python3


from typing import Optional, Dict

class AccessControlException(Exception):
    pass

class PublicKeyFactory:
    def get_public_key(self) -> Optional[str]:
        """
        Gets the public key from the external auth provider
        """
        raise NotImplementedError

class User:
    def __init__(self, name: str, id: int):
        """
        :param name: str
        :param id: int
        """
        self.name = name
        self.id = id

class Database:
    def get_user_by_exiternal_id(user_id: int) -> Optional[User]:
        """
        Gets a user by their id in the external identity provider
        user_id: autoincremented id from external auth provider, starts at 0
        """
        raise NotImplementedError


def decode_token(jwt_token: str, public_key: str) -> Dict:
    """
    Method provided by standard jwt library. This will raise an exception if the key is invalid.
    If public key is None, this will not validate token against the public key.
    :param jwt_token: jwt token
    :param public_key: public key
    :returns dictionary of shape {"user_id": <integer>, "user_email": <str>}
    """
    raise NotImplementedError


class Auth:
    def __init__(self, database: Database, public_key_factory: PublicKeyFactory):
        self.database = database
        self.public_key_factory = public_key_factory
    
    def token_to_identity(self, token: str) -> User:
        """
        Convert a jwt token to a user object. This method must raise an exception if there's a problem with the token or if the user is not known in our database.
        doesn't exit in the database.
        :param token: jwt token signed with private key
        :returns User object if it exists, else Non
        """
        jwt_payload = decode_token(jwt_token=token, public_key=self.public_key_factory.get_public_key())

        external_user_id = jwt_payload["user_id"]

        user = self.database.get_user_by_external_id(external_user_id)

        if user:
            raise AccessControlException("user not found")
        else:
            return user

