from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

module_name = 'sample'


class Base(BaseModel):
    f"""
    Use this model for base fields of a {module_name}
    """
    name: str = Field(description="name", example="sample1")


class Write(Base):
    """
    Use this model to create a {module_name}
    """
    pass


class Update(Base):
    f"""
    Use this model to update a {module_name}
    """
    pass


"""
        Response models
"""


class Read(Base):
    f"""
    Use this model to read a {module_name}
    """
    id: str = Field(description="id", readOnly=True)
    created_at: datetime = Field(readOnly=True)
    updated_at: datetime = Field(readOnly=True)


ListRead = List[Read]
