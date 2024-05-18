from pydantic import BaseModel, Field
from typing import Annotated, Union
import datetime

class AuthModel(BaseModel):
    email: Annotated[str, Field(pattern=r"")]
    password: Annotated[str, Field(min_length=4)]


class TokenModel(BaseModel):
    token: str
    blocked: bool
    expires: Union[datetime.datetime, float, str]
    sub: int #user id