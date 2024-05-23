import datetime
from typing import List, Union, Annotated, Optional
from pydantic import BaseModel, Field


class ProjectsModel(BaseModel):
    name: str
    description: Annotated[str | None, Field(min_length=2)] = None
    category_id: Annotated[int | None, Field(min=1)] = None
    user_id: Annotated[int, Field(min=0)]
    profile_id: Annotated[int, Field(min=0)]
    tags: list[str] | None = None
    createdAt: datetime.datetime | None = None
    launch_date: datetime.datetime | None = datetime.datetime.utcnow()
    need_investores: bool = True