from typing import Annotated
from pydantic import BaseModel, Field
from .profiles_model import ProfileModel


class UserModel(BaseModel):
    first_name: Annotated[str, Field(min_length=2)]
    last_name: Annotated[str, Field(min_length=2)]
    email: Annotated[str, Field(pattern=r"")]
    password: Annotated[str, Field(min_length=4)]
    user_type: Annotated[int, Field(min=1, max=10)]
    profile_id: Annotated[int, Field(gt=0)]
