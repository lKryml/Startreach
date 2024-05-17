from typing import Annotated, Optional
from pydantic import BaseModel, Field
from .profiles_model import ProfileModel


class UsersTypesModel(BaseModel):
    DEFAULT: int = 1
    COMPANY: int = 2
    INVESTOR: int = 3
    GOVERMENT: int = 4
    NGO: int = 5
    EDUCATION: int = 6
    SYNDICATE: int = 7

UserTypes = UsersTypesModel()

class UserModel(BaseModel):
    id: Optional[int | None] = None
    first_name: Annotated[str | None, Field(min_length=2)] = None
    last_name: Annotated[str | None, Field(min_length=2)] = None
    email: Annotated[str, Field(pattern=r"")]
    password: Annotated[str, Field(min_length=4)]
    user_type: Annotated[int, Field(min=1, max=10)] = UserTypes.DEFAULT
    profile_id: Annotated[int, Field(gt=0)]


class UserAuthenticatedModel(UserModel):
    access_token: str
    refresh_token: str
