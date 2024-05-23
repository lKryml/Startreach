from pydantic import BaseModel, Field
from typing import Annotated, Union
import datetime

class CategoriesModel(BaseModel):
    name: Annotated[str, Field(min_length=2)]
    parent_id: Annotated[int | None, Field(min=1)] = None
    img: Annotated[str | None, Field(min_length=4)] = None