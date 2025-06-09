from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from app.db_models.consts import UserStatus, UserRole
from typing import Optional

module_name = 'user'


class Base(BaseModel):
    f"""
    Use this model for base fields of a {module_name}
    """


class Register(Base):
    f"""
    Use this model to create a {module_name}
    """
    username: str = Field(description="username", example="")
    app_name: str = Field(description="Jomlex", example="")
    app_version: str = Field(description="v1.0.0", example="")


class LoginGoogle(Base):
    f"""
    Use this model to create a {module_name}
    """
    email: str = Field(description="email of user")
    name: str = Field(description="name of user")
    pic: str = Field(description="pic of user")
    app_name: str = Field(description="Jomlex", example="")
    app_version: str = Field(description="v1.0.0", example="")


class Login(Base):
    f"""
    Use this model to create a {module_name}
    """
    username: str = Field(description="Username of user", example="admin")
    password: str = Field(description="Password of user (will be hashed)", example="123456")


class ForgotPassword(Base):
    f"""
    Use this model to create a {module_name}
    """
    username: str = Field(description="Username or Email or Mobile of user", example="admin@gmail.com")


class ResetPassword(Base):
    f"""
    Use this model to create a {module_name}
    """
    email: str = Field(description="Email of user", example="admin@gmail.com")
    code: str = Field(description="Temporary code received by email", example="1000")
    new_password: str = Field(description="New password for user", example="123123")


class Write(Base):
    f"""
    Use this model to create a {module_name}
    """
    name: str = Field(description="Name of user", example="Ehsan")
    family: str = Field(description="Family of user", example="Rezaee")
    email: str = Field(description="Email of user", example="admin@gmail.com")
    mobile: str = Field(description="Mobile of user", example="+989151112233")
    role: UserRole = Field(description="Role id of user", example=UserRole.Player)
    avatar: str = Field(description="Avatar pic of user", example="pic.jpg")
    status: UserStatus = Field(description="Status of user", default=UserStatus.Enabled)
    username: str = Field(description="Username of user", example="admin")
    password: str = Field(description="Password of user (will be hashed)", example="123456")


class Read(Base):
    f"""
    Use this model to read a {module_name}
    """
    id: str = Field(description="id", readOnly=True)
    created_at: datetime = Field(readOnly=True)
    updated_at: datetime = Field(readOnly=True)

    name: str = Field(description="Name of user", example="Ehsan")
    family: str = Field(description="Family of user", example="Rezaee")
    email: str = Field(description="Email of user", example="admin@gmail.com")
    mobile: str = Field(description="Mobile of user", example="+989151112233")
    last_login: datetime = Field(description="last_login of user", readOnly=True)
    email_verified: bool = Field(description="Is email verified?", readOnly=True)
    mobile_verified: bool = Field(description="Is mobile verified?", readOnly=True)
    role: UserRole = Field(description="Role id of user", example=UserRole.Player)
    avatar: str = Field(description="Avatar pic of user", example="pic.jpg")
    status: UserStatus = Field(description="Status of user", default=UserStatus.Enabled)
    username: str = Field(description="Username of user", example="admin")


class Update(Base):
    f"""
    Use this model to update a {module_name}
    """
    name: Optional[str] = Field(None, description="Name of user", example="Ehsan")
    family: Optional[str] = Field(None, description="Family of user", example="Rezaee")
    email: Optional[str] = Field(None, description="Email of user", example="admin@gmail.com")
    mobile: Optional[str] = Field(None, description="Mobile of user", example="+989151112233")
    email_verified: Optional[bool] = Field(None, description="Is email verified?")
    mobile_verified: Optional[bool] = Field(None, description="Is mobile verified?")
    role: Optional[UserRole] = Field(None, description="Role id of user", example=UserRole.Player)
    avatar: Optional[str] = Field(None, description="Avatar pic of user", example="pic.jpg")
    status: Optional[UserStatus] = Field(None, description="Status of user")
    username: Optional[str] = Field(None, description="Username of user", example="admin")
    password: Optional[str] = Field(None, description="Password of user (will be hashed)", example="123456")


ListRead = List[Read]
