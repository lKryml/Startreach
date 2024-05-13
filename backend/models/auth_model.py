from pydantic import BaseModel, Field
from typing import Annotated

class AuthModel(BaseModel):
    email: Annotated[str, Field(pattern=r"")]
    password: Annotated[str, Field(min_length=4)]
