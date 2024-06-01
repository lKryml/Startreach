from pydantic import BaseModel, Field
from typing import Annotated

class LocationModel(BaseModel):
    lang: Annotated[int, Field(ge=0)]
    lat: Annotated[int, Field(ge=0)]