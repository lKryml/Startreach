from typing import List, Union, Annotated
from pydantic import BaseModel, Field


class ProfileModel(BaseModel):
    name: str
    email: str
    avatar: str
    description: str
    phones: List[str]