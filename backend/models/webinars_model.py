import datetime
from .global_model import LocationModel
from typing import Annotated
from pydantic import BaseModel, Field

class WebinarsModel(BaseModel):
    name: str
    description: Annotated[str | None, Field(min_length=2)] = None
    category_id: Annotated[int | None, Field(min=1)] = None
    user_id: Annotated[int | None, Field(min=0)] = None
    profile_id: Annotated[int | None, Field(min=0)] = None
    tags: list[str] | None = None
    createdAt: datetime.datetime | None = None
    start_date: datetime.datetime | None = datetime.datetime.utcnow()
    end_date: datetime.datetime | None = datetime.datetime.utcnow()
    attendens: Annotated[int | None, Field(min=0)] = 0
    guests: Annotated[list[str] | None, Field(min=0)] = []
    location: LocationModel