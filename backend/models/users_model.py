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
    ALL:int = 100

UserTypes = UsersTypesModel()

class UserModel(BaseModel):
    id: Optional[int | None] = None
    first_name: Annotated[str | None, Field(min_length=2)] = None
    last_name: Annotated[str | None, Field(min_length=2)] = None
    email: Annotated[str, Field(pattern=r"")]
    password: Annotated[str, Field(min_length=4)]
    user_type: Annotated[int, Field(min=0, max=10)] = 0 # if not set then the user should complete inserting information
    profile_id: Annotated[int | None, Field(ge=0)] = None
    is_superuser: Optional[bool | None] = False
    profile: Optional[ProfileModel | None] = None

class UserAuthenticatedModel(UserModel):
    access_token: str
    refresh_token: str
