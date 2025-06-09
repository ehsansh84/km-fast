from typing import List

from passlib.context import CryptContext

from app.core.base_db import DB
from app.db_models.consts import (UserStatus, UserRole)
from datetime import datetime

module_name = 'user'
module_text = 'User'


class User(DB):
    f"""
    Use this model to manage a {module_text}
    """

    def __init__(self, _id=None, module_name=module_name, module_text=module_text, db=None,
                 role=UserRole.Player, family='', email='', username='', password='', avatar='', country_code='',
                 last_login=datetime.now(), status=UserStatus.Enabled, name='', mobile='', email_verified=False,
                 mobile_verified=False, ip='', country='', region='', isp=''):
        self._id: str = _id

        self.ip: str = ip
        self.country: str = country
        self.region: str = region
        self.isp: str = isp
        self.role: UserRole = role
        self.name: str = name
        self.family: str = family
        self.email: str = email
        self.country_code: str = country_code
        self.mobile: str = mobile
        self.username: str = username
        self.password: str = password
        self.avatar: str = avatar
        self.last_login: datetime = last_login
        self.status: UserStatus = status
        self.email_verified: bool = email_verified
        self.mobile_verified: bool = mobile_verified
        self.__password_is_hashed = False

        super().__init__(_id=_id, module_name=module_name, module_text=module_text, db=db)

    def list(self, query=None, page_size=None) -> List['User']:
        return super().list(query=query, page_size=page_size)

    def hash_password(self):
        if not self.__password_is_hashed:
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            self.password = pwd_context.hash(self.password)
            self.__password_is_hashed = True

    def before_insert(self):
        if self.password:
            self.hash_password()

    def before_update(self):
        if self.password:
            self.hash_password()
