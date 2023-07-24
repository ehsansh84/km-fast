from typing import List
from pydantic import BaseModel, Field

module_name = 'user'


class Base(BaseModel):
    f"""
    Base model for {module_name}
    """
    name: str = Field(description="name of user", example="Ehsan")
    family: str = Field(description="family of user", example="Shirzadi")
    age: int = Field(description="age of user", example=38)


class Write(Base):
    f"""
    Use this model to create a {module_name}
    """
    username: str = Field(description="username", example="test-user")
    password: str = Field(description="password", example="ehsan@123")

    class Config:
        validate_assignment = True


class Read(Base):
    f"""
    Use this model to read a {module_name}
    """
    id: str = Field(description="user_id of owner", example="62d7a781d8f8d7627ce212d5")
    created_at: str = Field(readOnly=True)
    updated_at: str = Field(readOnly=True)
    username: str = Field(description="username", example="")


class Update(Base):
    f"""
    Use this model to update a {module_name}
    """


ListRead = List[Read]
